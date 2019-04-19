from flask import Flask, jsonify, render_template
import educationLoad
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')



@app.route("/asian")
def test():
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
def test2():
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
        "y": educationLoad.hispanic_home['No parents'].tolist(),
        "name": "No parents"
    }

    data = [trace1, trace2, trace3, trace4]

    return jsonify(data)

@app.route("/black")
def test3():
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
        "y": educationLoad.black_home_df['No parents'].tolist(),
        "name": "No parents"
    }

    data = [trace1, trace2, trace3, trace4]

    return jsonify(data)

@app.route("/white")
def test4():
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
        "y": educationLoad.white_home_df['No parents'].tolist(),
        "name": "No parents"
    }

    data = [trace1, trace2, trace3, trace4]

    return jsonify(data)

@app.route("/college")
def test5():
    trace1 = {
        "x": educationLoad.college_enrollment_data_df['Year'].tolist(),
        "y": educationLoad.college_enrollment_data_df['White non-Hispanic'],
        "name":"White"
    }

    trace2 = {
        "x": educationLoad.college_enrollment_data_df['Year'].tolist(),
        "y": educationLoad.college_enrollment_data_df['Black non-Hispanic'],
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
        "y": educationLoad.college_enrollment_data_df['Two or more races'],
        "name":"Two or more races"
    }
    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7]

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
