import subprocess
import os


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
        current_dir = '.' + os.getcwd() + '/ourDictionary'
        os.chdir('/')
        aspell_process = subprocess.run(['aspell', '-d', current_dir, '-a'], capture_output=True, text=True, input=word)
        if aspell_process.stdout.find("*") != -1:
            return True
        else:
            output = aspell_process.stdout.split(":")[1].split(', ')
            output[0] = output[0].lstrip()
            return output[:5]

    @staticmethod
    def createDictionaryFromDatabase(sender=None):
        if not SpellCheckService.make_file_unix():
            return
        else:
            dictionary_path = f"{os.getcwd()}/ourDictionary.multi"
            temp_path = f"{os.getcwd()}/linuxdict.file"
            aspell_process = f"aspell --lang=pl --dont-validate-words create master {dictionary_path} < {temp_path}"

            try:
                res = subprocess.check_output([aspell_process], shell=True)
            except subprocess.CalledProcessError as e:
                pass

            SpellCheckService.delete_file(temp_path)
            SpellCheckService.delete_file('dict.txt')
