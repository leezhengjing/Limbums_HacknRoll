from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "some secret string"

class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email(), Length(min=8, message="Email is not long enough!")])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")

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

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    else:
        return render_template("login.html", form=login_form)



if __name__ == "__main__":
    app.run(debug=True)