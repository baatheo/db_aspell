from flask import Blueprint
from flaskr.services.read_file import readFileAndCreateDB

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    readFileAndCreateDB()
    return "Hello world!"


@bp.route('/<string:name>')
def hello(name):
    return f"Hello, {name.capitalize()}"
