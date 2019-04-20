from flask import Flask, request, jsonify, render_template, redirect, url_for
import book_data, censusLoad, educationLoad



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
        

        return (x1 , df_variable1)

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
        
  
        return (y1 , df_variable2)
        
        


@app.route("/regrplot", methods=['GET','POST'])
def regrplot():
    df_variable1 = request.args['df_variable1']

    if df_variable1 in book_fields:
        x1 = book_data.year_book_data
    if df_variable1 in census1_fields:
        x1 = censusLoad.df_full1
    if df_variable1 in census2_fields:
        x1 = censusLoad.df_full2
    
    df_variable2 = request.args['df_variable2']
            
    if df_variable2 in book_fields:
        y1 = book_data.year_book_data
    if df_variable2 in census1_fields:
        y1 = censusLoad.df_full1
    if df_variable2 in census2_fields:
        y1 = censusLoad.df_full2

    Reg_df = x1.merge(y1, how = "inner", left_on ='year', right_on = 'year')
    plot = sns.regplot(x=f'{df_variable1}', y=f'{df_variable2}', data = Reg_df)
    fig = plot.get_figure()
    fig.savefig('regrplot', format='png')
    
    return redirect(url_for("regression.html"))

        
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
def index3():
    return render_template('index_test_button_census.html')

@app.route("/asian")
def test6():
    trace1 = {
        "x": educationLoad.asian_home_df['Year'].tolist(),
        "y": educationLoad.asian_home_df['Mother only'].tolist(),
        "name": "Mother only"        
    }

    trace2 = {
        "x": educationLoad.asian_home_df['Year'].tolist(),
        "y": educationLoad.asian_home_df['Father only'].tolist(),
        "name": "Father only"          
    }

    trace3 = {
        "x": educationLoad.asian_home_df['Year'].tolist(),
        "y": educationLoad.asian_home_df['Two married parents'].tolist(),
        "name": "Two married parents"          
    }    

    trace4 = {
        "x": educationLoad.asian_home_df['Year'].tolist(),
        "y": educationLoad.asian_home_df['No parent'].tolist(),
        "name": "No parent"          
    } 

    data = [trace1, trace2, trace3, trace4]

    return jsonify(data)

@app.route("/hispanic")
def test7():
    trace1 = {
        "x": educationLoad.hispanic_T['Year'].tolist(),
        "y": educationLoad.hispanic_home['Mother only'].tolist(),
        "name": "Mother only"
    }

    trace2 = {
        "x": educationLoad.hispanic_T['Year'].tolist(),
        "y": educationLoad.hispanic_home['Father only'].tolist(),
        "name": "Father only"
    }

    trace3 = {
        "x": educationLoad.hispanic_T['Year'].tolist(),
        "y": educationLoad.hispanic_home['Two married parents'].tolist(),
        "name": "Two married parents"
    }

    trace4 = {
        "x": educationLoad.hispanic_T['Year'].tolist(),
        "y": educationLoad.hispanic_home['No parent'].tolist(),
        "name": "No parents"
    }

    data = [trace1, trace2, trace3, trace4]

    return jsonify(data)

@app.route("/black")
def test8():
    trace1 = {
        "x": educationLoad.black_home_df['Year'].tolist(),
        "y": educationLoad.black_home_df['Mother only'].tolist(),
        "name": "Mother only"
    }

    trace2 = {
        "x": educationLoad.black_home_df['Year'].tolist(),
        "y": educationLoad.black_home_df['Father only'].tolist(),
        "name": "Father only"
    }

    trace3 = {
        "x": educationLoad.black_home_df['Year'].tolist(),
        "y": educationLoad.black_home_df['Two married parents'].tolist(),
        "name": "Two married parents"
    }

    trace4 = {
        "x": educationLoad.black_home_df['Year'].tolist(),
        "y": educationLoad.black_home_df['No parent'].tolist(),
        "name": "No parents"
    }

    data = [trace1, trace2, trace3, trace4]

    return jsonify(data)

@app.route("/white")
def test9():
    trace1 = {
        "x": educationLoad.white_home_df['Year'].tolist(),
        "y": educationLoad.white_home_df['Mother only'].tolist(),
        "name": "Mother only"
    }

    trace2 = {
        "x": educationLoad.white_home_df['Year'].tolist(),
        "y": educationLoad.white_home_df['Father only'].tolist(),
        "name": "Father only"
    }

    trace3 = {
        "x": educationLoad.white_home_df['Year'].tolist(),
        "y": educationLoad.white_home_df['Two married parents'].tolist(),
        "name": "Two married parents"
    }

    trace4 = {
        "x": educationLoad.white_home_df['Year'].tolist(),
        "y": educationLoad.white_home_df['No parent'].tolist(),
        "name": "No parents"
    }

    data = [trace1, trace2, trace3, trace4]

    return jsonify(data)

@app.route("/college")
def test10():
    trace1 = {
        "x": educationLoad.college_enrollment_data_df['Year'].tolist(),
        "y": educationLoad.college_enrollment_data_df['White non-Hispanic'],
        "name":"White"
    }

    trace2 = {
        "x": educationLoad.college_enrollment_data_df['Year'].tolist(),
        "y": educationLoad.college_enrollment_data_df['Black non-Hispanic '],
        "name":"Black"
    }

    trace3 = {
        "x": educationLoad.college_enrollment_data_df['Year'].tolist(),
        "y": educationLoad.college_enrollment_data_df['Hispanic'],
        "name":"Hispanic"
    }

    trace4 = {
        "x": educationLoad.college_enrollment_data_df['Year'].tolist(),
        "y": educationLoad.college_enrollment_data_df['Asian non-Hispanic'],
        "name":"Asian"
    }

    trace5 = {
        "x": educationLoad.college_enrollment_data_df['Year'].tolist(),
        "y": educationLoad.college_enrollment_data_df['Pacific Islander non-Hispanic'],
        "name":"Pacific Islander"
    }

    trace6 = {
        "x": educationLoad.college_enrollment_data_df['Year'].tolist(),
        "y": educationLoad.college_enrollment_data_df['American Indian/Alaska Native non-Hispanic'],
        "name":"American Indian"
    }

    trace7 = {
        "x": educationLoad.college_enrollment_data_df['Year'].tolist(),
        "y": educationLoad.college_enrollment_data_df['Two or more races non-Hispanic'],
        "name":"Two or more races"
    }
    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7]

    return jsonify(data)


@app.route("/education")
def index4():
    return render_template('index_education.html')


if __name__ == "__main__":
    app.run(debug=True)