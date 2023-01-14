from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/details")
def details():

    # if request.method == "POST":
    #     job_type = request.form.get("job_type")
    #     requirement = request.form.get("requirement")
    #     job_sector = request.form.get("job_sector")
    #     pay = request.form.get("pay")
    #     desc = request.form.get("desc")
    #
    #     return redirect ("/")
    # else:
    return render_template("details.html")


if __name__ == "__main__":
    app.run(debug=True)