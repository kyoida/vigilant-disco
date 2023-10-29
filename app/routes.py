from flask import render_template
from app import app, db
from app.models import User, Work

@app.route('/')
def index():
    users = User.query.all()
    works = Work.query.all()
    return render_template('user.html', users=users, works=works)

@app.route('/works/<int:user_id>')
def user_works(user_id):
    user = User.query.get(user_id)
    works = Work.query.filter_by(user_id=user_id)
    return render_template('works.html', user=user, works=works)
