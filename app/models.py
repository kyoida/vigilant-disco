from app import db

class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    user_cars = db.relationship("Work", back_populates="author")

    def __repr__(self):
        return f"User(user_id={self.user_id!r}, username={self.username!r})"


class Work(db.Model):
    __tablename__ = "works"
    work_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    author = db.relationship("User", back_populates="user_cars")

    def __repr__(self):
        return f"Work(work_id={self.work_id!r}, title={self.title!r})"

