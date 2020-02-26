import subprocess
import os

# funkcja przyjmuje jako argument String i zwraca tablice propozycji poprawy tego słowa
# jeżeli słowo należy do słownika zwraca True
from flaskr.services.dictionary_service import DictionaryService


def checkWord(word):
    current_dir = '.' + os.getcwd() + '/test'
    os.chdir('/')
    aspell_process = subprocess.run(['aspell', '-d', current_dir, '-a'], capture_output=True, text=True, input=word)
    if aspell_process.stdout.find("*") != -1:
        return True
    else:
        output = aspell_process.stdout.split(":")[1].split(', ')
        output[0] = output[0].lstrip()
        return output[:5]

def delete_file(sciezkaDoPliku):
    if os.path.isfile(sciezkaDoPliku):
            os.unlink(sciezkaDoPliku)
    else:
        print("cant delete sth that dosent exist")

def make_file_unix():
    proc = "tr -d '\\r' < dict.txt > linuxdict.file "
    res = subprocess.check_output(['bash','-c',proc])


def createDictionaryFromDatabase():
    make_file_unix()
    dictionary_path = os.getcwd() + '/ourDicrionary'
    text_database_path = os.getcwd() + '/linuxdict.file'
    aspell_process = "aspell --lang=en create master " + dictionary_path + " < " + text_database_path
    res = subprocess.check_output(['bash', '-c', aspell_process])
    delete_file('linuxdict.file')
    delete_file('dict.txt')




