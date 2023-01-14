from market import app

if __name__ == '__main__':
    app.run(debug=True)

# Dealing with photos
# app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'
# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, photos)


# class LoginForm(FlaskForm):
#     email = StringField(label='email',
#                         validators=[DataRequired(), Email(), Length(min=8, message="Email is not long enough!")])
#     password = PasswordField(label='password', validators=[DataRequired()])
#     submit = SubmitField(label="Log In")
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


