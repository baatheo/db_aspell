from . import db


class WordFile(db.Model):
    __tablename__ = 'word_file'
    word_id = db.Column(db.Integer, db.ForeignKey('word.id'), primary_key=True)
    file_id = db.Column(db.Integer, db.ForeignKey('file.id'), primary_key=True)
    counter = db.Column(db.Integer)
