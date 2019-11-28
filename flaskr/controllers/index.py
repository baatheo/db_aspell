from flask import Blueprint, render_template, request, json, jsonify
from flaskr.services.read_file import readFileAndCreateDB
from flaskr.services.spell_check import checkWord

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return render_template('base.html', action="/upload", w="")


@bp.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    typeOfFile = file.headers['content-type']
    content = str(file.read())
    content = content[2:-1]

    if typeOfFile == "text/plain":
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


@bp.route('/verify', methods=['POST', 'GET'])
def verify():
    if (not request.data):
        error = "Empty payload"
        return jsonify(error=error)

    wordJson = request.json
    wordList = []
    for i in wordJson:
        word = i['word']
        tempJson = {
            'word': word,
            'reply': checkWord(word)
        }
        wordList.append(tempJson)
    return jsonify(results=wordList, length=len(wordList))


@bp.route('/<string:name>')
def hello(name):
    return f"Hello, {name.capitalize()}"
