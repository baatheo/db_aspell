from datetime import datetime as dt
from . import db


class File(db.Model):
    __tablename__ = 'file'
    id = db.Column(db.INTEGER, primary_key=True)
    created = db.Column(db.TIMESTAMP, nullable=False)
    name = db.Column(db.VARCHAR, nullable=False)

    def __repr__(self):
        return '<File {}>'.format(self.name)


def createFile(name):
    f = File(name=name, created=dt.now())
    db.session.add(f)
    db.session.commit()
    return f
