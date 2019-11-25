import re
import os
from flaskr.models.word import Word, createWord
from flaskr.models.file import File, createFile


def readFileAndCreateDB(file_name):
    file = open(file_name, "r")
    result = file.read()
    regex = re.sub(r'[^a-zA-Z0-9 ]', r'', result)
    words_list = regex.split()
    word_count = {}
    for word in words_list:
        if len(word) >= 2:
            word_count[word] = words_list.count(word)

    f = createFile(file_name)

    for x in word_count:
        createWord(x, f.id, word_count.__getitem__(x))

    file.close()
    os.remove(file_name)

    # TODO: napisać funkcję która przy dodawaniu nowych słów
    #  sprawdza czy takowe już się nie znajdują w bazie
    #  i tylko zwiększyć counter zamiast tworzyć nowy wpis

    # TODO: ogarnąć obsługę języka polskiego
