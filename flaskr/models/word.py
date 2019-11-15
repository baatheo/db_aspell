from . import db


class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
