from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, URL
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor, CKEditorField

##CONNECT TO DB
db = SQLAlchemy()
# create the app
app = Flask(__name__)
Bootstrap(app)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db"
# initialize the app with the extension
db.init_app(app)

class Products(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    tags = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all()


class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email(), Length(min=8, message="Email is not long enough!")])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")

@app.route("/")
def index():
    products = db.session.execute(db.select(Products).order_by(Products.title)).scalars()
    return render_template("index.html", products=products)

@app.route("/details")
def details():

    # Get data to hydrate the page
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