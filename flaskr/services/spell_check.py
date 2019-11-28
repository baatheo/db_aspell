import subprocess

#funkcja przyjmuje jako argument String i zwraca tablice propozycji poprawy tego słowa
#jezeli slowo nalezy do slownika zwraca True
def checkWord(word):
    p1 = subprocess.run(['aspell', '-a'], capture_output=True, text=True, input = word)
    if(p1.stdout.find("*")!=-1):
        return True
    else:
        output = p1.stdout.split(":")
        returnedWords =output[1].split(',')
        return returnedWords
print(checkWord('hells'))
