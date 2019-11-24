from flask import Blueprint, render_template, request
from flaskr.models.word import Word, createWord
from flaskr.models.file import File, createFile
from flaskr.services.read_file import readFileAndCreateDB


bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    f = createFile("first")
    w = createWord("tree", f.id, 20)
    readFileAndCreateDB("flaskr/file.txt")
    return render_template('base.html', action="/upload", w=w.word)

@bp.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    return file.filename


@bp.route('/<string:name>')
def hello(name):
    return f"Hello, {name.capitalize()}"
