import subprocess


# funkcja przyjmuje jako argument String i zwraca tablice propozycji poprawy tego słowa
# jeżeli słowo należy do słownika zwraca True
def checkWord(word):
    aspell_process = subprocess.run(['aspell', '-a'], capture_output=True, text=True, input=word)
    if aspell_process.stdout.find("*") != -1:
        return True
    else:
        output = aspell_process.stdout.split(":")[1].split(', ')
        output[0] = output[0].lstrip()
        return output[:5]
