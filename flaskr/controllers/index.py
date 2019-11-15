from flask import Blueprint
from flaskr.models.word import Word, createWord
from flaskr.models.file import File

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    w = createWord("tree")
    return "Hello world!" + str(w)


@bp.route('/<string:name>')
def hello(name):
    return f"Hello, {name.capitalize()}"
