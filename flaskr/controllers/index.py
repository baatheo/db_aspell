from flask import Blueprint

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return "Hello world!"


@bp.route('/<string:name>')
def hello(name):
    return f"Hello, {name.capitalize()}"
