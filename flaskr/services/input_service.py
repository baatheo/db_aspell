import re


class InputService:
    input_String = ""
    word_list = []
    output_word_list = []
    wordDict_list = []

    def setInputString(self, input):
        self.input_String = input
        self.setWordList()

    def setOutputWords(self):
        self.countRepeatingWords()
        self.deleteRepeatinWords()

    def getOutputWordList(self):
        return self.output_word_list

    def getWordList(self):
        return self.word_list

    def setWordList(self):
        self.word_list = re.sub(r'[^a-ząćęłńóśźżĄĆĘŁŃÓŚŹŻA-Z0-9\n ]', r'', self.input_String).split()

    def countRepeatingWords(self):
        for x in range(len(self.word_list)):
            wordDict = {}
            wordDict["word"] = self.word_list[x]
            wordDict["pos"] = []
            wordDict["pos"].append(x)
            wordDict["repeating"] = False
            if self.word_list[x] in self.word_list[0:x]:
                wordDict["repeating"] = True
                originalIndex = self.getIdOfOriginal(self.word_list[x], x)
                if originalIndex != -999:
                    self.wordDict_list[originalIndex]["pos"].append(x)
            self.wordDict_list.append(wordDict)

    def deleteRepeatinWords(self):
        for word in self.wordDict_list:
            if word["repeating"] is False:
                del word["repeating"]
                self.output_word_list.append(word)

    def getIdOfOriginal(self, word, index):
        for x in range(index):
            if self.word_list[x] == word:
                return x
        y = -999
        return y

