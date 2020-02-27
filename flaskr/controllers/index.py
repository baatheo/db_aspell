from flask import Blueprint, render_template, request, jsonify
from flaskr.services.spell_check import SpellCheckService
from flaskr.services.file_to_db_service import FileToDBService
from flaskr.services.dictionary_service import DictionaryService
from flaskr.services.signal_service import signalService
from flask.signals import signals_available

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

    # TODO @baatheo jak będzie inne kodowanie to się wyjebie. Zabezpiecz to jakiś try/catch
    content = str(file.read().decode('utf-8'))

    if typeOfFile == "text/plain":
        if len(content) == 0:
            return render_template('base.html', action="/upload", w="pusty plik sprobuj ponownie")
        else:
            fs = FileToDBService()
            fs.setFileContent(content)
            fs.setFileName(file.filename)
            fs.setWords()
            signalService.get_signal('file_written').connect(SpellCheckService.createDictionaryFromDatabase)
            DictionaryService.create_or_update_dictionary(signalService)

            return content
    else:
        return render_template('base.html', action="/upload", w="zły format pliku sprobuj ponownie")


@bp.route('/verify', methods=['POST', 'GET'])
def verify():
    if (not request.data):
        error = "Empty payload"
        return jsonify(error=error)

    wordJson = request.json
    wordList = []
    for word in wordJson:
        tempJson = {
            'word': word,
            'reply': SpellCheckService.checkWord(word)
        }
        wordList.append(tempJson)
    return jsonify(results=wordList, length=len(wordList))


@bp.route('/<string:name>')
def hello(name):
    return f"Hello, {name.capitalize()}"
