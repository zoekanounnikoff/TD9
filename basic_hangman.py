import random
AA = ("python", "information", "systems", "programming", "centralesupelec", "zoe", "nathan", "camille")
mot = random.choice(AA)
b = '' #ensemble des caractères déjà devinés par le joueur 
tries = 5

while tries > 0:
    d = 0 # nombre de caractères qu'il reste à deviner 
    for e in mot:
        if e in b:
            print (e)
        else :
            print ("*")
            d += 1 # on met le caractère s'il a déjà été deviné et une étoile sinon
    if d == 0:
        print ("You won")
        break
    f = input (" guess a character :")
    b += f
    if f not in mot:
        tries -= 1
        print ("Wrong , you have ", + tries, " more guesses ")
        if tries == 0:
            print ("You Lost , the word was: "+mot)

def compare(a,b):
    x = 0
    for lettre in a:
        if lettre in b:
            x += 1
    return (x == len(a))

def guesses(char, word, tries):
    if char in word:
        tries -= 1
    return(tries)

