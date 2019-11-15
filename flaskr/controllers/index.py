from flask import Blueprint
from flaskr.models.word import Word

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    w = Word()
    return "Hello world!"


@bp.route('/<string:name>')
def hello(name):
    return f"Hello, {name.capitalize()}"
