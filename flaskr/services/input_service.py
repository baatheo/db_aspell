import re


class InputService:
    input_string = ""
    word_list = []
    output_word_list = []
    wordDict_list = []

    def setInputString(self, input_text):
        self.input_string = input_text
        self.word_list = self.setWordList(self.input_string)

    def setOutputWords(self, incorrect_words):
        self.wordDict_list = []
        self.output_word_list = []
        self.word_list = incorrect_words
        self.countRepeatingWords()
        self.deleteRepeatinWords()

    def getOutputWordList(self):
        return self.output_word_list

    def getWordList(self):
        return self.word_list

    @staticmethod
    def setWordList(input_string):
        return re.sub(r'[^a-ząćęłńóśźżĄĆĘŁŃÓŚŹŻA-Z0-9\n ]', r'', input_string).split()

    def countRepeatingWords(self):
        for x in range(len(self.word_list)):
            wordDict = {}
            wordDict["word"] = self.word_list[x]
            wordDict["pos"] = []
            wordDict["pos"].append(x)
            wordDict["repeating"] = "not exist"
            if self.word_list[x] in self.word_list[0:x]:
                wordDict["repeating"] = "exist"
                originalIndex = self.getIdOfOriginal(self.word_list[x], x)
                if originalIndex != -999:
                    self.wordDict_list[originalIndex]["pos"].append(x)
            self.wordDict_list.append(wordDict)

    def deleteRepeatinWords(self):
        for word in self.wordDict_list:
            if word["repeating"] == "not exist":
                self.output_word_list.append(word)


    def getIdOfOriginal(self, word, index):
        for x in range(index):
            if self.word_list[x] == word:
                return x
        y = -999
        return y

