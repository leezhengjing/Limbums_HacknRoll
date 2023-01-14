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

class RegisterForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email(), Length(min=8, message="Email is not long enough!")])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/details")
def details():

    # Get data to hydrate the page
    return render_template("details.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()

    test_email = "admin@email.com"
    test_pass = "12345678"

    # Validate data
    if login_form.validate_on_submit():
        if login_form.email.data != test_email or login_form.password.data != test_pass:
            return render_template("login.html", form=login_form)
        else:
            return render_template("index.html")
    else:
        return render_template("login.html", form=login_form)

# Work in progress
@app.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    login_form = LoginForm()

    if register_form.validate_on_submit():
        email = register_form.email.data
        password = register_form.password.data

        return render_template("login.html", form=login_form)
    else:
        return render_template("register.html", form=register_form)

@app.route("/listings", methods=["GET", "POST"])
def listings():
    return render_template("sell.html")

@app.route("/sell", methods=["GET", "POST"])
def sell():
    return render_template("listings.html")

if __name__ == "__main__":
    app.run(debug=True)