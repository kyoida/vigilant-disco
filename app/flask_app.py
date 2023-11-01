from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\anels\OneDrive\Рабочий стол\python\ass3\vigilant-disco\app\user.db'

db = SQLAlchemy(app)

app.config['SECRET_KEY'] = "why do I need it"

# Create an application context
with app.app_context():
    # Now you can perform database operations within the context
    db.create_all()
