from flask import Flask, jsonify, render_template
import censusLoad
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/line")
def test():
    data = [{
        "x": censusLoad.df_full1['year'].tolist(),
        "y": censusLoad.df_full1['PopInPoverty'].tolist()}]

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
