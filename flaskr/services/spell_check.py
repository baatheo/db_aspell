import subprocess
import os
from pathlib import Path
import time


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
        process = f"echo {word} | aspell -a -d /mnt/c/Projects/db_aspell/ourDictionary"
        aspell_process = subprocess.Popen(process, shell=True, stdout=subprocess.PIPE)
        cmd_output = aspell_process.stdout.read().decode("utf-8")
        if cmd_output.find("*") != -1:
            return True
        # TODO zrub cos z tym bo sie wytrzymac nie da
        elif cmd_output.find("# ") != -1:
            return "brak podpowiedzi"
        else:
            output = cmd_output.split(":")[1].split(', ')
            output[0] = output[0].lstrip()
            if len(output) < 5:
                output[len(output) - 1] = output[len(output) - 1].replace('\n', '')
                return output[:len(output)]
            else:
                return output[:5]

    @staticmethod
    def createDictionaryFromDatabase(sender=None):
        if not SpellCheckService.make_file_unix():
            return
        else:
            dictionary_path = f"{os.getcwd()}/ourDictionary"
            temp_path = f"{os.getcwd()}/linuxdict.file"
            aspell_process = f"aspell --lang=pl --encoding=utf-8 create master {dictionary_path} < {temp_path}"
            try:
                res = subprocess.check_output([aspell_process], shell=True)
                SpellCheckService.delete_file(temp_path)
                SpellCheckService.delete_file('dict.txt')
            except subprocess.CalledProcessError as e:
                return False

    @staticmethod
    def checkDictionaryIfExists():
        if os.path.isfile(str(Path(os.getcwd()).parents[1]) + '/ourDictionary'):
            return True
        else:
            return False
