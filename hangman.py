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
