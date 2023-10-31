from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'


with app.app_context():
    db.init_app(app)

app.config['SECRET_KEY'] = "why do i need it"
db.init_app(app)