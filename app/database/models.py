from flask_app import db
from datetime import datetime

class User(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Clolumn(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)

    user_works = db.relationship("Work", back_populates="owner", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"User(id{self.id!r}, name={self.name!r}"


class Works(db.Model):
    __tablename__= "works"
    work_id = db.Column(db.Integer, primary_key=True)
    work_title = db.Column(db.String(100), nullable=False)
    work_text = db.Column(db.Text, nullable=False)
    work_date = db.Column(db.DateTime, default=datetime.utcnow)
    work_owner = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    owner = db.relationship("User", back_populates="user_works")

    def __repr__(self):
        return f"Work(work_id={self.works.work_id!r}, work_title={self.works.work_title!r}, work_text={self.works.work_text!r}, work_date={self.works.work_date!r}), work_owner={self.works.work_owner!r}"




