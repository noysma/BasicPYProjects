import random
from hard import hard
from easy import easy
import hangmanart as art
import string

# Choose the difficulty
while True:
    check = input('Choose the difficulty!! easy or hard? ')
    check = check.lower()
    if check == 'easy':
        words = easy
        print('You choose EASY!\n')
        break
    elif check == 'hard':
        words = hard
        print('You choose HARD!!\n')
        break
    else:
        print('\n- Choose a valid parameter\n')

# Game
print(art.logo)
print()
def valid(words):
    word = random.choice(words)  # randomly chooses a word
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = valid(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # user guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1
                print('\The letter you choose is not in the word ('+ user_letter +')')
                print(art.stages[lives])

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nNOT A VALID LETTER!')

    if lives == 0:
        print('You lost. The word was', word)
    else:
        print('You guessed the word', word + '. GOOD JOB!!')


if __name__ == '__main__':
    hangman()