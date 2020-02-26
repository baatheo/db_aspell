import os
import re

from flaskr.models.file import createFile
from flaskr.models.word import createOrUpdateWord


class FileToDBService:
    file_name = None
    file_content = None
    word_list = []

    def setFileName(self, file_name):
        self.file_name = file_name

    def setFileContent(self, content):
        self.file_content = content

    def setWords(self):
        if self.file_content is not None:
            self.parseFileContent()
            self.createDB()

    def saveFromFile(self):
        if self.file_name is not None:
            self.readFile()
            self.setWords()
            self.removeFile()

    def readFile(self):
        file = open(self.file_name, "r")
        self.file_content = file.read()
        file.close()

    def removeFile(self):
        os.remove(self.file_name)

    def parseFileContent(self):
        self.word_list = re.sub(r'[^a-ząćęłńóśźżĄĆĘŁŃÓŚŹŻA-Z0-9\n ]', r'', self.file_content).split()

    def createDB(self):
        file = createFile(self.file_name)

        for word in self.word_list:
            if len(word) >= 2:
                createOrUpdateWord(word=word, file=file)
