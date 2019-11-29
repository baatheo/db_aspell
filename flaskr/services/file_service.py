import re
import os
from flaskr.models.word import Word, createOrUpdateWord
from flaskr.models.file import File, createFile


class FileService:

    file_name = None
    file_content = None
    word_list = []

    def setFileName(self, file_name):
        self.file_name = file_name

    def setFileContent(self, content):
        self.file_content = content

    def saveFromContent(self):
        if self.file_content is not None:
            self.parseFileContent()
            self.createDB()

    def saveFromFile(self):
        if self.file_name is not None:
            self.readFile()
            self.saveFromContent()
            self.removeFile()

    def readFile(self):
        file = open(self.file_name, "r")
        self.file_content = file.read()
        file.close()

    def removeFile(self):
        os.remove(self.file_name)

    def parseFileContent(self):
        self.word_list = re.sub(r'[^a-zA-Z0-9 ]', r'', self.file_content).split()

    def createDB(self):
        file = createFile(self.file_name)

        for word in self.word_list:
            if len(word) >= 2:
                createOrUpdateWord(word=word, file=file)
