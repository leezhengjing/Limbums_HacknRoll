from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, URL
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_ckeditor import CKEditor, CKEditorField

class RegisterForm(FlaskForm):
    username = StringField(label='username')
    email_address = StringField(label='email')
    password1 = PasswordField(label='password1')
    password2 = PasswordField(label='password2')
    submit = SubmitField(label='submit')

class LoginForm(FlaskForm):
    email = StringField(label='email',
                        validators=[DataRequired(), Email(), Length(min=8, message="Email is not long enough!")])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")

class CreatePostForm(FlaskForm):
    title = StringField("Name of Product", validators=[DataRequired()])
    tags = StringField("Tags", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Item Description", validators=[DataRequired()])
    submit = SubmitField("Submit Post")
#
#
# class UploadForm(FlaskForm):
#     photo = FileField(
#         validators=[
#             FileAllowed(photos, "Only images are allowed"),
#             FileRequired("File field should not be empty")
#         ]
#     )
#     submit = SubmitField("Upload")