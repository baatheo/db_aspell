from datetime import datetime as dt
from . import db
from .pivot_word_file import wordFile


class Word(db.Model):

    __tablename__ = 'word'
    id = db.Column(db.INTEGER, primary_key=True)
    word = db.Column(db.VARCHAR, nullable=False)
    created = db.Column(db.TIMESTAMP, nullable=False)
    file = db.relationship('File', secondary=wordFile, lazy='subquery',
                           backref=db.backref('words', lazy=True))

    def __repr__(self):
        return '<Word {}>'.format(self.word)


def createWord(word):
    w = Word(word=word, created=dt.now())
    db.session.add(w)
    db.session.commit()
    return w
