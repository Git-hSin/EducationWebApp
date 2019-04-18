from flask import Flask, request, jsonify, render_template
import book_data, censusLoad

app = Flask(__name__)

@app.route("/dropdown")
def dropdownList():
    book_fields= list(book_data.year_book_data)
    census1_fields = list(censusLoad.df_full1)
    census2_fields = list(censusLoad.df_full2)

    dropdown_fields = book_fields + census1_fields + census2_fields
    return render_template('dropdown.html', dropdown_fields=dropdown_fields)


if __name__ == "__main__":
    app.run(debug=True)
