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


def createOrUpdateWord(word, file):
    word_exists = db.session.query(Word).filter_by(word=word).first()
    if word_exists is not None:
        word_id = word_exists.id
        file_id = file.id
        relation_exist = db.session.query(wordFile).filter_by(word_id=word_id, file_id=file_id).first()
        if relation_exist is not None:
            relation_exist.counter += 1
            # db.session.query(wordFile).filter_by()
            # db.session.commit()
        else:
            statement = wordFile.insert().values(word_id=word_id, file_id=file_id, counter=1)
            db.session.execute(statement)
            db.session.commit()
    else:
        w = Word(word=word, created=dt.now())
        db.session.add(w)
        db.session.commit()
        statement = wordFile.insert().values(word_id=w.id, file_id=file.id, counter=1)
        db.session.execute(statement)
        db.session.commit()
