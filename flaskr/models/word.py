from datetime import datetime as dt
from . import db


class Word(db.Model):

    __tablename__ = 'word'
    id = db.Column(db.INTEGER, primary_key=True)
    word = db.Column(db.VARCHAR, nullable=False)
    created = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return '<Word {}>'.format(self.word)


def createWord(word):
    w = Word(word=word, created=dt.now())
    db.session.add(w)
    db.session.commit()
    return w
