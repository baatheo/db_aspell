import os

from flaskr.models.__init__ import db
from flaskr.models.word import Word


def getWordsFromDB():
    words_list = []
    query = db.session.query(Word.word).all()

    for word in query:
        words_list.append(*word)

    return words_list


def getExistingWords(path):
    words_list = []
    file = open(path, 'r')
    data = file.readlines()

    for word in data:
        words_list.append(word[:-1])

    return words_list


def writeTxt(words_from_database, words_already_existing, path):
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


def createOrUpdateDictionary():
    path = "flaskr/services/dict.txt"
    writeTxt(getWordsFromDB(), getExistingWords(path), path)
