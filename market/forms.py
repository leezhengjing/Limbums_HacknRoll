from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, URL, EqualTo
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_ckeditor import CKEditor, CKEditorField

class RegisterForm(FlaskForm):
    username = StringField(label='username', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='email', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='password1', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='password2', validators=[EqualTo('password1')])
    submit = SubmitField(label='submit', render_kw={'style': 'background-color: blue; color: white;'})

class LoginForm(FlaskForm):
    email = StringField(label='email',
                        validators=[DataRequired(), Email(), Length(min=8, message="Email is not long enough!")])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField(label="Log In", render_kw={'style': 'background-color: blue; color: white;'})

class CreatePostForm(FlaskForm):
    name = StringField("Name of Product", validators=[DataRequired()])
    price = StringField("Price", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired()])
    description = CKEditorField("Item Description", validators=[DataRequired()])
    submit = SubmitField("Submit Post", render_kw={'style': 'background-color: blue; color: white;'})
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