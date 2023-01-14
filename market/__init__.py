from flask import Flask, render_template, send_from_directory, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, IMAGES, configure_uploads

# CONNECT TO DB
db = SQLAlchemy()
# create the app
app = Flask(__name__)

Bootstrap(app)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db"
# initialize the app with the extension
db.init_app(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# Dealing with photos
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)


# class UploadForm(FlaskForm):
#     photo = FileField(
#         validators=[
#             FileAllowed(photos, "Only images are allowed"),
#             FileRequired("File field should not be empty")
#         ]
#     )
#     submit = SubmitField("Upload")
#
#
# class LoginForm(FlaskForm):
#     email = StringField(label='email',
#                         validators=[DataRequired(), Email(), Length(min=8, message="Email is not long enough!")])
#     password = PasswordField(label='password', validators=[DataRequired()])
#     submit = SubmitField(label="Log In")

from market import routes