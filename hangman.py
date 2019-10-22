def get_guessed_word(secret_word, letters_guessed):
    mot = ''
    for k in range(len(secret_word)):
        if secret_word[k] in letters_guessed:
            mot += secret_word[k]
        else:
            mot += '*'
    return mot 

