def get_guessed_word(secret_word, letters_guessed):
    mot = ''
    for k in range(len(secret_word)):
        if secret_word[k] in letters_guessed:
            mot += secret_word[k]
        else:
            mot += '*'
    return mot 

def check_guessed_word(secret_word, letters_guessed):
    return secret_word == get_guessed_word(secret_word, letters_guessed)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def lettres_restantes(guesses):
    lettres =''
    for x in alphabet:
        if not (x in guesses):
            lettres += x
    return lettres 

def word_game(secret_word, tries):
    guesses = ''
    while tries > 0:
        if check_guessed_word(secret_word, guesses):
            print("Bravo ! Vous avez gagné ! Trop fort !")
            break
        mot = get_guessed_word(secret_word, guesses)
        print(mot)
        print("You have ", + tries, " tries left")
        print("Lettres restantes :")
        print(lettres_restantes(guesses))
        letter = input('Devinez une lettre')
        if len(letter) == 1:
            guesses += letter
            if letter in secret_word:
                print("Bien deviné !")
            else:
                print("Pas de chance...")
                tries -= 1
        else:
            print("Un seul caractère svp")
    print("Vous avez perdu déso")




