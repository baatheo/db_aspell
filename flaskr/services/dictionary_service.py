import os

from flaskr.services.signal_service import signalService
from flaskr.models import db
from flaskr.models.word import Word


class DictionaryService:

    @staticmethod
    def get_words_from_db():
        words_list = []
        query = db.session.query(Word.word).all()

        for word in query:
            words_list.append(*word)

        return words_list

    @staticmethod
    def get_existing_words(path):
        words_list = []
        file = open(path, 'r')
        data = file.readlines()

        for word in data:
            words_list.append(word[:-1])

        file.close()
        return words_list

    @staticmethod
    def write_txt(words_from_database, path):
        if os.path.isfile(path):
            words_list = DictionaryService.get_existing_words(path) + words_from_database
        else:
            words_list = words_from_database

        words_list.sort()
        file = open(path, 'w')

        for word in words_list:
            file.write(word)
            file.write('\n')

        file.close()
        file_written = signalService.get_signal('file_written')
        file_written.send()

    @staticmethod
    def create_or_update_dictionary():
        file_name = "dict.txt"
        DictionaryService.write_txt(DictionaryService.get_words_from_db(), file_name)
