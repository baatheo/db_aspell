from . import db


class Word(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.INTEGER, primary_key=True)
    word = db.Column(db.VARCHAR, nullable=False)
