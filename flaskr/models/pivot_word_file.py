from . import db


wordFile = db.Table('word_file',
    db.Column('word_id', db.Integer, db.ForeignKey('word.id'), primary_key=True),
    db.Column('file_id', db.Integer, db.ForeignKey('file.id'), primary_key=True),
    db.Column('counter', db.Integer)
)
