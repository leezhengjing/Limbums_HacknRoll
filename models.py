from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///products.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''


def db_drop_and_create_all(app):
    with app.app_context():
        db.drop_all()
        db.create_all()


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