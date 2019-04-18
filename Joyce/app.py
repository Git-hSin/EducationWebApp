from flask import Flask, request, jsonify, render_template
import book_data, censusLoad



import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)
sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = 20, 15

app = Flask(__name__)
    
book_fields= list(book_data.year_book_data)
census1_fields = list(censusLoad.df_full1)
census2_fields = list(censusLoad.df_full2)
dropdown_fields = book_fields + census1_fields + census2_fields

@app.route("/")
def index():
    return render_template('index_test_button.html')

@app.route("/dropdown")
def dropdownList():
    return render_template('dropdown.html', dropdown_fields=dropdown_fields)


@app.route("/dropdown_x", methods=['GET', 'POST'])
def testt1():
    if request.method == 'POST':
        df_variable1 = request.form['df_variable1']
        #df_variable2 = request.form['df_variable2']
        
        if df_variable1 in book_fields:
           x = book_data.year_book_data
        if df_variable1 in census1_fields:
           x = censusLoad.df_full1
        if df_variable1 in census2_fields:
           x = censusLoad.df_full2
        
        #if df_variable2 in book_fields:
        #   y = book_data.year_book_data
        #if df_variable2 in census1_fields:
        #   y = censusLoad.df_full1
        #if df_variable2 in census2_fields:
        #   y = censusLoad.df_full2
    return x

@app.route("/dropdown_y", methods=['GET', 'POST'])
def testt2():
    if request.method == 'POST':
        #df_variable1 = request.form['df_variable1']
        df_variable2 = request.form['df_variable2']
        
        #if df_variable1 in book_fields:
        #   x = book_data.year_book_data
        #if df_variable1 in census1_fields:
        #   x = censusLoad.df_full1
        #if df_variable1 in census2_fields:
        #   x = censusLoad.df_full2
        
        if df_variable2 in book_fields:
           y = book_data.year_book_data
        if df_variable2 in census1_fields:
           y = censusLoad.df_full1
        if df_variable2 in census2_fields:
           y = censusLoad.df_full2
    
    return y
        
        


@app.route("/regrplot", methods=['GET','POST'])
def regrplot():
    if request.method == 'POST':
        df_variable1 = request.form['df_variable1']
        df_variable2 = request.form['df_variable2']

        Reg_df = testt1().merge(testt2(), how = "inner", left_on ='year', right_on = 'year')
        plot = sns.regplot(x=f'{df_variable1}', y=f'{df_variable2}', data = Reg_df)
        plot.savefig('regrplot', format='png')
        
    return render_template("regression.html")

        

@app.route("/weeks", methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        tag = request.form['yr']
        if tag != '':
            date_filtered_df = book_data.year_book_data[book_data.year_book_data['last_year'] == float(tag)]
            data = [{
                "x": date_filtered_df['last_year'].tolist(),
                "y": date_filtered_df['weeks_on_list'].tolist()}]
        else:
            data = [{
            "x": book_data.year_book_data['last_year'].tolist(),
            "y": book_data.year_book_data['weeks_on_list'].tolist()}]
    else:
        data = [{
        "x": book_data.year_book_data['last_year'].tolist(),
        "y": book_data.year_book_data['weeks_on_list'].tolist()}]

    return jsonify(data)


@app.route("/count")
def test2():
    data = [{
        "x": book_data.year_book_data['last_year'].tolist(),
        "y": book_data.year_book_data['count'].tolist()}]

    return jsonify(data)
 
@app.route("/review")
def test3():
    data = [{
        "x": book_data.year_book_data['last_year'].tolist(),
        "y": book_data.year_book_data['Amazon_reviews'].tolist(),
        "type":'bar'}]

    return jsonify(data)

@app.route("/rating")
def test4():
    data = [{
        "x": book_data.year_book_data['last_year'].tolist(),
        "y": book_data.year_book_data['Amazon_rating'].tolist()}]

    return jsonify(data)

@app.route("/price")
def test5():
    data = [{
        "x": book_data.year_book_data['last_year'].tolist(),
        "y": book_data.year_book_data['Amazon_price'].tolist()}]

    return jsonify(data)

@app.route("/book")
def index2():
    return render_template('index_test_button_book.html')

if __name__ == "__main__":
    app.run(debug=True)
