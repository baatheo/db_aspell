import os

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

        return words_list

    @staticmethod
    def write_txt(words_from_database, words_already_existing, path):
        if os.path.isfile(path) is True:
            file = open(path, 'r+')
            w = words_already_existing + words_from_database
            w.sort()
            for word in w:
                file.write(word)
                file.write('\n')

        else:
            file = open(path, 'w')
            for word in words_from_database:
                file.write(word)
                file.write('\n')
        file.close()

    @staticmethod
    def create_or_update_dictionary():
        path = "flaskr/services/dict.txt"
        DictionaryService.write_txt(
            DictionaryService.get_words_from_db(),
            DictionaryService.get_existing_words(path), path)
