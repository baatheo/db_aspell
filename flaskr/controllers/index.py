from flask import Blueprint
from flaskr.models.word import Word, createWord
from flaskr.models.file import File, createFile

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    f = createFile("first")
    w = createWord("tree", f.id, 20)
    return "Hello world!" + str(w)


@bp.route('/<string:name>')
def hello(name):
    return f"Hello, {name.capitalize()}"
