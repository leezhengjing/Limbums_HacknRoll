from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/details")
def details():

    # Get data to hydrate the page
    return render_template("details.html")


if __name__ == "__main__":
    app.run(debug=True)