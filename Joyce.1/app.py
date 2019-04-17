from flask import Flask, request, jsonify, render_template
import book_data
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index_test.html')


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

if __name__ == "__main__":
    app.run(debug=True)
