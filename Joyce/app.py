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

        if df_variable1 in book_fields:
           x1 = book_data.year_book_data
        if df_variable1 in census1_fields:
           x1 = censusLoad.df_full1
        if df_variable1 in census2_fields:
           x1 = censusLoad.df_full2
        

        return x1

@app.route("/dropdown_y", methods=['GET', 'POST'])
def testt2():
    if request.method == 'POST':

        df_variable2 = request.form['df_variable2']
                
        if df_variable2 in book_fields:
           y1 = book_data.year_book_data
        if df_variable2 in census1_fields:
           y1 = censusLoad.df_full1
        if df_variable2 in census2_fields:
           y1 = censusLoad.df_full2
    
        return y1
        
        


@app.route("/regrplot", methods=['GET','POST'])
def regrplot():
    if request.method == 'POST':
        df_variable1 = request.form['df_variable1']
        df_variable2 = request.form['df_variable2']

        if df_variable1 in book_fields:
            x1 = book_data.year_book_data
        if df_variable1 in census1_fields:
            x1 = censusLoad.df_full1
        if df_variable1 in census2_fields:
            x1 = censusLoad.df_full2

        if df_variable2 in book_fields:
            y1 = book_data.year_book_data
        if df_variable2 in census1_fields:
            y1 = censusLoad.df_full1
        if df_variable2 in census2_fields:
            y1 = censusLoad.df_full2

        Reg_df = x1.merge(y1, how = "inner", left_on ='year', right_on = 'year')
        plot = sns.regplot(x=f'{df_variable1}', y=f'{df_variable2}', data = Reg_df)
        plot.savefig('regrplot', format='png')
        
    return render_template("regression.html")

        
@app.route("/line1_c")
def plot1_c():
    data = [{
        "x": censusLoad.df_full1['year'].tolist(),
        "y": censusLoad.df_full1['PopInPoverty'].tolist()}]
    return jsonify(data)


@app.route("/line2_c")
def plot2_c():
    data = [{
        "x": censusLoad.df_full1['year'].tolist(),
        "y": censusLoad.df_full1['PopEmployed'].tolist()}]
    return jsonify(data)

@app.route("/line3_c")
def plot3_c():
    data = [{
        "x": censusLoad.df_full1['year'].tolist(),
        "y": censusLoad.df_full1['EstMeanIncAll'].tolist()}]
    return jsonify(data)

@app.route("/line4_c")
def plot4_c():
    data = [{
        "x": censusLoad.df_full2['year'].tolist(),
        "y": censusLoad.df_full2['PropVal'].tolist()}]
    return jsonify(data)

@app.route("/line5_c")
def plot5_c():
    data = [{
        "x": censusLoad.df_full2['year'].tolist(),
        "y": censusLoad.df_full2['Population'].tolist()}]
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

@app.route("/census")
def index2():
    return render_template('index_test_button_census.html')

if __name__ == "__main__":
    app.run(debug=True)