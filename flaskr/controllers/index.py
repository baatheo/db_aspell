from flask import Blueprint, render_template, request, jsonify, make_response
from flaskr.services.spell_check import SpellCheckService
from flaskr.services.file_to_db_service import FileToDBService
from flaskr.services.dictionary_service import DictionaryService
from flaskr.services.signal_service import signalService
from flask.signals import signals_available
import os

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return render_template('base.html', action="/upload", w="")


@bp.route('/signals_available')
def sa():
    return f"{signals_available}"


@bp.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    typeOfFile = file.headers['content-type']
    errors = []
    if typeOfFile == "text/plain":
        try:
            content = str(file.read().decode('utf-8'))
        except UnicodeDecodeError:
            errors.append("Cant decode content of file")
            form = {'errors': errors, 'success': False}
            return make_response(jsonify(form=form), 422)
        if len(content) == 0:
            errors.append("empty payload")
            form = {'errors': errors, 'success': False}
            return make_response(jsonify(form=form), 422)
        else:
            fs = FileToDBService()
            fs.setFileContent(content)
            fs.setFileName(file.filename)
            fs.setWords()
            signalService.get_signal('file_written').connect(SpellCheckService.createDictionaryFromDatabase)
            DictionaryService.create_or_update_dictionary()
            form = {'message': "File uploaded successfully", 'success': True}
            return make_response(jsonify(form=form), 201)
    else:
        errors.append("Wrong file format")
        form = {'errors': errors, 'success': False}
        return make_response(jsonify(form=form), 422)


@bp.route('/verify', methods=['POST', 'GET'])
def verify():
    if not request.data:
        errors = []
        errors.append("empty payload")
        form = {'errors': errors}
        return make_response(jsonify(form=form), 422)
    if not SpellCheckService.checkDictionaryIfExists():
        errors = []
        errors.append("Aspell dictionary don't exsist")
        form = {'errors': errors}
        return make_response(jsonify(form=form), 503)

    #TODO dopracować do końca pobieranie słów i przekazanie do przetwarzania
    wordJson = request.json
    wordList = []
    for i in wordJson:
        word = i['word']
        tempJson = {
            'word': word,
            'reply': SpellCheckService.checkWord(word)
        }
        wordList.append(tempJson)
    form = {'success': "Returned words", 'results': wordList, 'length': len(wordList)}
    return make_response(jsonify(form=form))


@bp.route('/<string:name>')
def hello(name):
    return f"Hello, {name.capitalize()}"
