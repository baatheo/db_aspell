from flask import Blueprint, render_template, request

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return render_template('base.html', action="/upload")


@bp.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    return file.filename


@bp.route('/<string:name>')
def hello(name):
    return f"Hello, {name.capitalize()}"
