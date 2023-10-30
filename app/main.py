from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from . import app, db
from .models import User
from flask_login import login_user, login_required, logout_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

@app.route('/')
def main():
    return render_template('base.html')


@app.route('/portfolio')
def portfolio():
    return render_template('works.html')

@app.route("/user/<int:user_id>")
def user_page(user_id):
    user = User.query.get(user_id)
    if user:
        return render_template("users.html", user=user)
    else:
        return "User not found"


@app.route('/login', methods=['GET', 'POST'])
def login(context=None):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()

        if user:
            login_user(user)
            return redirect(url_for('user_page', user_id=user.user_id))
        else:
            return render_template('login.html', context='The login or username were wrong')

    return render_template('login.html', context=context)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
