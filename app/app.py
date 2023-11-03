from flask import render_template, request, redirect, url_for, session
from database.models import User, Work  # Assuming you've renamed Works to Work
from flask_app import db, app
from database.crud import add_user, add_work, delete_work, get_all_works, get_all_users


# Main route
@app.route('/')
def index():
    return render_template('index.html')


# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        login = request.form['login']
        name = request.form['name']

        # Check if user already exists
        existing_user = User.query.filter_by(login=login).first()
        if existing_user:
            # Handle user already exists
            return render_template('registration.html', error='Login already exists')

        new_user = User(login=login, name=name)
        add_user(new_user)

        # Log in the user by setting a session variable
        session['user_id'] = new_user.id

        return redirect(url_for('user_profile', user_id=new_user.id))
    return render_template('registration.html')


# Log in route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        # Here you should check the user's password as well, which is not implemented in your current model
        user = User.query.filter_by(login=login).first()
        if user:
            # Log the user in by setting the user_id in the session
            session['user_id'] = user.id
            return redirect(url_for('index'))  # Redirect to the homepage or dashboard
        else:
            error = 'Invalid username'
            return render_template('login.html', error=error)

    return render_template('login.html')

# User profile route
@app.route('/user/<int:user_id>', methods=['GET'])
def user_profile(user_id):
    user = User.query.get_or_404(user_id)
    works = Work.query.filter_by(work_owner=user_id).all()

    return render_template('user.html', user=user, works=works)

# Log out route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))


# Explore route
@app.route('/explore')
def explore():
    works = get_all_works()
    return render_template('explore.html', works=works)


# Create work route
@app.route('/create-work', methods=['GET', 'POST'])
def create_work():
    if request.method == 'POST':
        work_title = request.form['work_title']
        work_text = request.form['work_text']

        # You need to retrieve the user from the session
        user_id = session.get('user_id')
        if not user_id:
            # Redirect to login if no user is logged in
            return redirect(url_for('login'))

        new_work = Work(work_title=work_title, work_text=work_text, work_owner=user_id)
        add_work(new_work)

        return redirect(url_for('user_profile', user_id=user_id))
    return render_template('create_work.html')


# Delete work route
@app.route('/delete-work/<int:work_id>')
def delete_work_route(work_id):
    work = Work.query.get_or_404(work_id)
    if session.get('user_id') != work.work_owner:
        # Handle case where the logged-in user is not the owner of the work
        return "Unauthorized", 403

    delete_work(work)
    return redirect(url_for('user_profile', user_id=session['user_id']))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
