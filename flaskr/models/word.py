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


def createWord(word, file, counter):
    w = Word(word=word, created=dt.now())
    # w.append(file)
    db.session.add(w)
    db.session.commit()
    statement = wordFile.insert().values(word_id=w.id, file_id=file, counter=counter)
    db.session.execute(statement)
    db.session.commit()
    return w
