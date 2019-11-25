from flask import Blueprint, render_template, request, jsonify
from flaskr.models.word import Word, createWord
from flaskr.models.file import File, createFile
from flaskr.services.read_file import readFileAndCreateDB
import io

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    f = createFile("first")
    w = createWord("tree", f.id, 20)
    return render_template('base.html', action="/upload", w=w.word)


@bp.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    typ = file.headers['content-type']
    zawartosc = str(file.read())
    zawartosc = zawartosc[2:-1]

    if typ == "text/plain":
        if len(zawartosc) == 0:
            return render_template('base.html', action="/upload", w="pusty plik sprobuj ponownie")
        else:
            plik = open('flaskr/file.txt', 'w+')
            plik.write(zawartosc)
            plik.close()
            readFileAndCreateDB("flaskr/file.txt")
            return zawartosc
    else:
        return render_template('base.html', action="/upload", w="zły format pliku sprobuj ponownie")


@bp.route('/<string:name>')
def hello(name):
    return f"Hello, {name.capitalize()}"
