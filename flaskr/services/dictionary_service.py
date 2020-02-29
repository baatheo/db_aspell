import os
import io

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
        file = io.open(path, 'r', encoding='utf8')
        data = file.readlines()

        for word in data:
            words_list.append(word[:-1])

        file.close()
        return words_list

    @staticmethod
    def write_txt(words_list, path):
        words_list.sort()
        file = io.open(path, 'w', encoding='utf8')

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
