
def checkOpLetter(woord, lettering):
    for letter in range(len(woord)):
        if woord[letter] == lettering:
            return True
    return False



hetjuistewoord = 'fiets'
print("Welkom bij Lingo")
print("Raadt het woord")
print(".....")

for x in range(5):
    invoer = input("wat is je letter?")
    if checkOpLetter(hetjuistewoord, invoer):
        print("je hebt het goed")
    else:
        print("je hebt het niet zo goed!")