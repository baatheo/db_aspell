import subprocess

#funkcja przyjmuje jako argument String i zwraca tablice propozycji poprawy tego słowa
#jezeli slowo nalezy do slownika zwraca True
def checkWord(word):
    p1 = subprocess.run(['aspell', '-a'], capture_output=True, text=True, input = word)
    if(p1.stdout.find("*")!=-1):
        return True
    else:
        p2 = p1.stdout.translate({ord(i): None for i in ' '})
        output = p2.split(":")
        returnedWords =output[1].split(',')
        print(returnedWords[:5])
        return returnedWords


