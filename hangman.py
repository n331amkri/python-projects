import random

from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    print(word)
    word_letters = set(word) #letters in the word
    
    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ') #could also use set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed
     
    #getting user input
    while len(word_letters) > 0:
        print('Current word:', ' '.join([letter if letter in used_letters else '-' for letter in word]))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')
    print('Congratulations! You guessed the word', word, '!')

hangman()