"""
Name: Brendan Kratt
hw9.py

Problem: This program defines various functions that make up the component parts of a game of
         hangman. The preceding functions are used within the two final functions, one being
         a command line interface and the other a GUI.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from random import randint
def get_words(file_name):
    file = open(file_name, "r")
    lst_words = []
    for i in file:
        lst_words.append(i)
    return lst_words

def get_random_word(words):
    output = words[randint(0, (len(words)-1))]
    output = output.strip("\n")
    return output

def letter_in_secret_word(letter, secret_word):
    for i in secret_word:
        if i == letter:
            return True
    return False


def already_guessed(letter, guesses):
    for i in guesses:
        if i == letter:
            return True
    return False


def make_hidden_secret(secret_word, guesses):
    output = ""
    for i in secret_word:
        if i in guesses:
            output += i
        else:
            output += "_"
        output += " "
    return output.strip()


def won(guessed):
    if "_" in guessed:
        return False
    return True


def play_graphics(secret_word):
    pass

def play_command_line(secret_word):
    guesses_lst = []
    guesses_remain = 6
    guessed_correct = make_hidden_secret(secret_word, guesses_lst)
    while guesses_remain > 0 and not guessed_correct == secret_word:
        print("already guessed:", guesses_lst)
        print("guesses remaining:", guesses_remain)
        print(guessed_correct)
        curr_guess = input("guess a letter: ")
        guesses_lst.append(curr_guess)
        if letter_in_secret_word(curr_guess, secret_word):
            guessed_correct = make_hidden_secret(secret_word, guesses_lst)
        guesses_remain -= 1
        if guessed_correct.split(" ") == list(secret_word):
            print("winner!\n" + guessed_correct)
            break
        elif guesses_remain == 0:
            print("sorry, you did not guess the word.")
            print("the secret word was", secret_word)
        else:
            print()


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
