from database.models import User, Work, db

def add_user(user: User) -> None:
    db.session.add(user)
    db.session.commit()

def delete_user(user: User) -> None:
    db.session.delete(user)
    db.session.commit()

def add_work(work: Work) -> None:
    db.session.add(work)
    db.session.commit()

def delete_work(work: Work) -> None:
    db.session.delete(work)
    db.session.commit()

def get_all_works() -> db.Query:
    return Work.query.all()

def get_all_users() -> db.Query:
    return User.query.all()