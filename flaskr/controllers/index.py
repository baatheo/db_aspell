from flask import Blueprint, render_template, request, jsonify, make_response
from flaskr.services.spell_check import SpellCheckService
from flaskr.services.file_to_db_service import FileToDBService
from flaskr.services.dictionary_service import DictionaryService
from flaskr.services.signal_service import signalService
from flask.signals import signals_available
from flaskr.services.input_service import InputService

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return render_template('base.html', title="GNU Aspell based, online spell checker")


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
            DictionaryService.create_or_update_dictionary()
            form = {'message': "File uploaded successfully", 'success': True}
            return make_response(jsonify(form=form), 201)
    else:
        errors.append("Wrong file format")
        form = {'errors': errors, 'success': False}
        return make_response(jsonify(form=form), 422)


@bp.route('/verify', methods=['POST', 'GET'])
def verify():
    # if not request.form:
    #     errors = []
    #     errors.append("empty payload")
    #     form = {'errors': errors}
    #     return make_response(jsonify(form=form), 422)

    # rawContent = request.form
    content = request.form.get('textInput')
    incorrect_words = []
    input = InputService()
    input.setInputString(content)
    inputWords = input.getWordList()
    output_dict_list = {}
    for word in inputWords:
        if SpellCheckService.checkWord(word) is not True:
            incorrect_words.append(word)

    input.setOutputWords(incorrect_words)
    output_word_list = input.getOutputWordList()
    for word in output_word_list:
        wordDict = {}
        wordDict = {
            "list": SpellCheckService.checkWord(word["word"]),
            "pos": word["pos"]
        }
        output_dict_list[word["word"]] = wordDict
    return make_response(jsonify(output_dict_list), 200)
