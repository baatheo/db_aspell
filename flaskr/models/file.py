from . import db


class File(db.Model):

    __tablename__ = 'file'
    id = db.Column(db.INTEGER, primary_key=True)
    created = db.Column(db.TIMESTAMP, nullable=False)
    name = db.Column(db.VARCHAR, nullable=False)
