from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\anels\OneDrive\Рабочий стол\python\ass3\vigilant-disco\app\instance\users.db'
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = "why do I need it"

with app.app_context():
    db.create_all()
