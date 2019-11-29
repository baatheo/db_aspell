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
    exists = db.session.query(db.exists().where(Word.word == word)).scalar()
    print(exists)
    if exists:
        id = db.select(Word.id).filter(Word.word == word).one()
        db.update(wordFile).where(wordFile.word_id == id).values(wordFile.counter + counter)
    else:
        w = Word(word=word, created=dt.now())
        db.session.add(w)
        db.session.commit()
        statement = wordFile.insert().values(word_id=w.id, file_id=file, counter=counter)
        db.session.execute(statement)
        db.session.commit()
        return w
