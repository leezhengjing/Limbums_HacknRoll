from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///products.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


def db_drop_and_create_all(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

# class User(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     username = db.Column(db.String(length=30), nullable=False, unique=True)
#     email_address = db.Column(db.String(length=50), nullable=False, unique=True)
#     password_hash = db.Column(db.String(length=60), nullable=False)
#     products = db.relationship('Products', backref='owned_user', lazy=True)



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

    def __init__(self, title, body):
        self.name = title
        self.body = body

# with app.app_context():
#     db.create_all()