

from flask import Flask, render_template
from database.models import Users

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page " + name + " - " + str(id)


# @app.route('/registration', method={"POST", "GET"})
# def registration():
#
#

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
