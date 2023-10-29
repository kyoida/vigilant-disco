from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/users'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__='students'
    username = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    password = db.Column(db.String(40))

    def __init__(self, username, name, password):
        self.username = username
        self.name = name
        self.password = password




@app.route('/')
def base():
    return render_template('base.html')

@app.route('/explore')
def expore():
    return render_template('users.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/account')
def account():
    if request.method == 'POST':
        # Handle registration or sign-in here
        if 'register' in request.form:
            username = request.form['username']
            name = request.form['name']
            password = request.form['password']
            # Add the registration logic here (create a new User record)
            print(username)
            print(name)
            print(password)
        elif 'login' in request.form:
            username = request.form['username']
            password = request.form['password']
            # Add the sign-in logic here (verify the user's credentials)
            user = User.query.filter_by(username=username, password=password).first()
            if user:
                # User is signed in, you can redirect to a different page or display a message
                return "Welcome, " + user.username
            else:
                return "Invalid credentials, please try again."

    return render_template('acc.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
