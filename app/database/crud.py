from database.models import User, Work, db  # Changed 'Works' to 'Work'

def add_user(user: User) -> None:
    db.session.add(user)
    db.session.commit()

def delete_user(user: User) -> None:
    db.session.delete(user)
    db.session.commit()

def add_work(work: Work) -> None:  # Changed 'Works' to 'Work'
    db.session.add(work)
    db.session.commit()

def delete_work(work: Work) -> None:  # Changed 'Works' to 'Work'
    db.session.delete(work)
    db.session.commit()

def get_all_works() -> db.Query:  # Removed unused parameter
    return Work.query.all()  # Changed 'Works' to 'Work'

def get_all_users() -> db.Query:  # Removed unused parameter
    return User.query.all()