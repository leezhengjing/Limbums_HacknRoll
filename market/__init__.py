from flask import Flask, render_template, send_from_directory, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor

# CONNECT TO DB
db = SQLAlchemy()
# create the app
app = Flask(__name__)

Bootstrap(app)
CKEditor(app)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db"
# initialize the app with the extension
db.init_app(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


from market import routes