# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Load configuration from config.py
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

# Other app setup code...

