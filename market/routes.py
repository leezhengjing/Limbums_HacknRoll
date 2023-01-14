from market import app
from flask import render_template, request, Response
from market.models import Products
from market import db
from market.forms import RegisterForm, LoginForm

from bot import tel_send_image, tel_send_message, tel_parse_message


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        print("Hello")
        msg = request.get_json()
        try:
            chat_id, txt = tel_parse_message(msg)
            if txt == "good am":
                tel_send_message(chat_id, "Good am!")
            elif txt == "products":
                products = db.session.execute(db.select(Products).order_by(Products.title)).scalars()
                tel_send_message(chat_id, str(products))
            else:
                tel_send_image(chat_id)
        except:
            print("from index-->")

        return Response('ok', status=200)
    else:
        products = db.session.execute(db.select(Products).order_by(Products.title)).scalars()
        return render_template("index.html", products=products)

    # https://api.telegram.org/bot5972375728:AAHGXbdkAqdmIGGbOul6Ds4BrJQMqOISRRY/setWebhook?url=xs-2.opensvr.net


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
        email = register_form.email_address.data
        password = register_form.password1.data

        return render_template("login.html", form=login_form)
    else:
        return render_template("register.html", form=register_form)


@app.route("/listings", methods=["GET", "POST"])
def listings():
    products = db.session.execute(db.select(Products).order_by(Products.title)).scalars()
    return render_template("listings.html", products=products)


# Getting filename from url
@app.route('/sell/<filename>')
def get_file(filename):
    return "hello world"


# return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)


@app.route("/sell", methods=["GET", "POST"])
def sell():
    # upload_form = UploadForm()
    #
    # if upload_form.validate_on_submit():
    #     filename = photos.save(upload_form.photo.data)
    #     file_url = url_for('get_file', filename=filename)
    # else:
    #     file_url = None
    #
    #     return render_template("sell.html", form=upload_form, file_url=file_url)
    return "hello world"
