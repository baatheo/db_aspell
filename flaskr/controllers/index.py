from flask import Blueprint, render_template, request
from flaskr.services.file_service import FileService

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return render_template('base.html', action="/upload", w="")


@bp.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    typeOfFile = file.headers['content-type']

    # TODO @baatheo jak będzie inne kodowanie to się wyjebie. Zabezpiecz to jakiś try/catch
    content = str(file.read().decode('utf-8'))

    if typeOfFile == "text/plain":
        if len(content) == 0:
            return render_template('base.html', action="/upload", w="pusty plik sprobuj ponownie")
        else:
            fs = FileService()
            fs.setFileContent(content)
            fs.setFileName(file.filename)
            fs.saveFromContent()
            return content
    else:
        return render_template('base.html', action="/upload", w="zły format pliku sprobuj ponownie")


@bp.route('/<string:name>')
def hello(name):
    return f"Hello, {name.capitalize()}"
