from models import User, Works,  db


def add_user(user:User) -> None:
    db.session.add(user)
    db.session.commit()


def delete_user(user:User) -> None:
    db.session.delete(user)
    db.session.commit()


def add_work(work:Works) -> None:
    db.session.add(work)
    db.session.commit()



def delete_work(work:Works)->None:
    db.session.delete(work)
    db.session.commit()


def get_all_works(work: Works) -> db.Query:
    return Works.query.all()


def get_all_users(user: User) -> db.Query:
    return User.query.all()
