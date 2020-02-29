import subprocess
import os
from pathlib import Path
import time


class SpellCheckService:

    dict_file_name = "ourDictionary.rws"

    @staticmethod
    def delete_file(path):
        if os.path.isfile(path):
            os.unlink(path)
        else:
            print("Can't delete file that doesn't exists.")

    @staticmethod
    def make_file_unix():
        print(os.path.isfile(Path('dict.txt')))
        script = "tr -d '\\r' < dict.txt > linuxdict.file "
        try:
            subprocess.call(script, shell=True)
        except subprocess.CalledProcessError as e:
            raise Exception("Can't create linuxdict.file")

    @staticmethod
    def createDictionaryFromDatabase(sender=None):
        SpellCheckService.make_file_unix()
        dictionary_path = f"{os.getcwd()}/{SpellCheckService.dict_file_name}"
        temp_path = f"{os.getcwd()}/linuxdict.file"
        aspell_process = f"aspell --lang=pl --encoding=utf-8 create master {dictionary_path} < {temp_path}"
        try:
            res = subprocess.check_output([aspell_process], shell=True)
            SpellCheckService.delete_file(temp_path)
            SpellCheckService.delete_file('dict.txt')
            return dictionary_path
        except subprocess.CalledProcessError as e:
            raise Exception("Can't create ourDictionary.rws")

    @staticmethod
    def checkWord(word):
        process = f"echo {word} | aspell -a -d {os.getcwd()}/{SpellCheckService.dict_file_name}"
        aspell_process = subprocess.Popen(process, shell=True, stdout=subprocess.PIPE)
        cmd_output = aspell_process.stdout.read().decode("utf-8")
        print(cmd_output)
        if cmd_output.find("*") != -1:  # słowo należy do słownika
            return True
        elif cmd_output.find("# ") != -1:  # słowo nie należy do słownika i nie ma podpowiedzi dla niego
            return "brak podpowiedzi"
        elif cmd_output == "":  # jakiś błąd
            raise Exception("Empty cmd_output", cmd_output)
        else:  # znaleziono propozycje dla słowa
            output = cmd_output.split(":")[1].split(', ')
            output[0] = output[0].lstrip()
            if len(output) < 5:
                output[len(output) - 1] = output[len(output) - 1].replace('\n', '')
                return output[:len(output)]
            else:
                return output[:5]

    @staticmethod
    def checkDictionaryIfExists():
        if os.path.isfile(str(Path(os.getcwd()).parents[1]) + '/ourDictionary'):
            return True
        else:
            return False
