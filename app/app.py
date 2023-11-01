from flask import Flask, render_template, request, redirect, url_for
from database.models import User, Works, db
from flask_app import app
from database.crud import add_user, add_work, delete_work, get_all_works, get_all_users


@app.route('/')
def index():
    return render_template('index.html')


# Define route for registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get user input from the registration form
        login = request.form['login']
        name = request.form['name']

        # Create a new User object and add it to the database
        new_user = User(login=login, name=name)
        add_user(new_user)

        # You can add additional logic, like session management, here
        return redirect(url_for('login'))  # Redirect to login page after registration
    return render_template('registration.html')


# Define route for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check the user's credentials (you may want to implement authentication logic)
        login = request.form['login']
        user = User.query.filter_by(login=login).first()
        if user:
            # You can add authentication logic here
            # For example, set a session variable to identify the logged-in user
            return redirect(url_for('user'))
        else:
            # Handle invalid login
            return render_template('login.html', error='Invalid login')
    return render_template('login.html')


# Define route for creating a work
# @app.route('/create-work', methods=['GET', 'POST'])
# def create_work():
#     if request.method == 'POST':
#         # Get user input from the work creation form
#         work_title = request.form['work_title']
#         work_text = request.form['work_text']
#
#         # Create a new Work object and add it to the database
#         new_work = Works(work_title=work_title, work_text=work_text,
#                          work_owner=1)  # Replace 1 with the actual user's ID
#         add_work(new_work)
#         return redirect(url_for('user'))
#     return render_template('create_work.html')
#
#
# # Define route for deleting a work
# @app.route('/delete-work/<int:work_id>')
# def delete_work(work_id):
#     work = Works.query.get(work_id)
#     if work:
#         delete_work(work)
#         return redirect(url_for('user'))
#     else:
#         # Handle work not found
#         return redirect(url_for('user'))
#

# Define a route for the user profile
@app.route('/user')
def user():
    # Retrieve the user's works and other user-specific information
    works = get_all_works()
    users = get_all_users()
    return render_template('user.html', works=works, users=users)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
