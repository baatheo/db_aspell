from flask import Blueprint, render_template, request
from flaskr.models.word import Word, createWord
from flaskr.models.file import File, createFile
from flaskr.services.read_file import readFileAndCreateDB

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    f = createFile("first")
    w = createWord("tree", f.id, 20)
    return render_template('base.html', action="/upload", w=w.word)


@bp.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    type = file.headers['content-type']
    content = str(file.read())
    content = content[2:-1]

    if type == "text/plain":
        if len(content) == 0:
            return render_template('base.html', action="/upload", w="pusty plik sprobuj ponownie")
        else:
            fileToWrite = open('flaskr/file.txt', 'w+')
            fileToWrite.write(content)
            fileToWrite.close()
            readFileAndCreateDB("flaskr/file.txt")
            return content
    else:
        return render_template('base.html', action="/upload", w="zły format pliku sprobuj ponownie")


@bp.route('/<string:name>')
def hello(name):
    return f"Hello, {name.capitalize()}"
