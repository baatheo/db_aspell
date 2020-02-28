import subprocess
import os
from pathlib import Path


class SpellCheckService:

    @staticmethod
    def delete_file(path):
        if os.path.isfile(path):
            os.unlink(path)
        else:
            print("Can't delete file that doesn't exists.")

    @staticmethod
    def make_file_unix():
        proc = "tr -d '\\r' < dict.txt > linuxdict.file "
        try:
            res = subprocess.check_output([proc], shell=True)
            return True
        except subprocess.CalledProcessError as e:
            return False

    @staticmethod
    def checkWord(word):
        temp_path = os.getcwd()
        current_dir = '.' + str(Path(temp_path).parents[1]) + '/ourDictionary'
        os.chdir(str(Path(temp_path).parents[1]))
        aspell_process = subprocess.run(['aspell', '-d', './ourDictionary', '-a'], capture_output=True, text=True, input=word)
        if aspell_process.stdout.find("*") != -1:
            return True
        else:
            output = aspell_process.stdout.split(":")[1].split(', ')
            output[0] = output[0].lstrip()
            if len(output) < 5:
                output[len(output)-1] = output[len(output)-1].replace('\n','')
                return output[:len(output)]
            else:
                return output[:5]

    @staticmethod
    def createDictionaryFromDatabase(sender=None):
        if not SpellCheckService.make_file_unix():
            return
        else:
            print(os.getcwd())
            dictionary_path = f"{os.getcwd()}/ourDictionary"

            temp_path = f"{os.getcwd()}/linuxdict.file"
            aspell_process = f"aspell --lang=pl --encoding=utf-8 create master {dictionary_path} < {temp_path}"
            try:
                res = subprocess.check_output([aspell_process], shell=True)
            except subprocess.CalledProcessError as e:
                return False
            SpellCheckService.delete_file(temp_path)
            SpellCheckService.delete_file('dict.txt')
