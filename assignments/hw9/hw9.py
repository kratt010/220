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
from graphics import GraphWin, Circle, Line, Text, Point, Entry

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
    win_width = 550
    win_height = 550
    win = GraphWin("Hangman", win_width, win_height)
    win.setBackground("white")

    floor_pt1 = Point(win_width / 2 - 100, 400)
    floor_pt2 = Point(win_width / 2 + 50, 400)
    floor = Line(floor_pt1, floor_pt2)
    floor.draw(win)

    vert_polept1 = Point(win_width / 2, 400)
    vert_polept2 = Point(win_width / 2, 50)
    vert_pole = Line(vert_polept1, vert_polept2)
    vert_pole.draw(win)

    horiz_polept1 = vert_polept2.clone()
    horiz_polept2 = Point(floor_pt1.getX(), 50)
    horiz_pole = Line(horiz_polept1, horiz_polept2)
    horiz_pole.draw(win)

    rope_polept1 = horiz_polept2.clone()
    rope_polept2 = Point(rope_polept1.getX(), 100)
    rope_pole = Line(rope_polept1, rope_polept2)
    rope_pole.draw(win)

    head_center = Point(rope_polept2.getX(), 125)
    head = Circle(head_center, 25)

    body_pt1 = Point(head_center.getX(), 150)
    body_pt2 = Point(body_pt1.getX(), 250)
    body = Line(body_pt1, body_pt2)

    right_leg_pt1 = body_pt2.clone()
    right_leg_pt2 = Point(win_width / 2 - 50, 300)
    right_leg = Line(right_leg_pt1, right_leg_pt2)

    left_leg_pt1 = right_leg_pt1.clone()
    left_leg_pt2 = Point(win_width / 2 - 150, 300)
    left_leg = Line(left_leg_pt1, left_leg_pt2)

    right_arm_pt1 = body.getCenter()
    right_arm_pt2 = Point(win_width / 2 - 150, 225)
    right_arm = Line(right_arm_pt1, right_arm_pt2)

    left_arm_pt1 = right_arm_pt1.clone()
    left_arm_pt2 = Point(win_width / 2 - 50, 225)
    left_arm = Line(left_arm_pt1, left_arm_pt2)

    guess_prompt_pt = Point(win_width / 2 - 75, win_height - 75)
    guess_prompt = Text(guess_prompt_pt, "Guess a letter:")
    guess_prompt.draw(win)

    guessed_incorrect_str = ""
    guessed_incorrect_pt = Point(450, win_height / 2 - 100)
    guessed_incorrect = Text(guessed_incorrect_pt, guessed_incorrect_str)
    guessed_incorrect.draw(win)

    guess_entry_pt = Point(win_width / 2, guess_prompt_pt.getY())
    guess_entry = Entry(guess_entry_pt, 4)
    guess_entry.draw(win)

    guesses_lst = []
    guesses_remain = 6

    guessed_correct = make_hidden_secret(secret_word, guesses_lst)
    guessed_correct_txt_pt = Point(win_width / 2 - 75, win_height - 100)
    guessed_correct_txt = Text(guessed_correct_txt_pt, guessed_correct)
    guessed_correct_txt.draw(win)
    while guesses_remain >= 0 and not guessed_correct == secret_word:

        win.getKey()
        curr_guess = guess_entry.getText()
        guess_entry.setText("")
        guesses_lst.append(curr_guess)
        if letter_in_secret_word(curr_guess, secret_word):
            guessed_correct = make_hidden_secret(secret_word, guesses_lst)
            guessed_correct_txt.undraw()
            guessed_correct_txt = Text(guessed_correct_txt_pt, guessed_correct)
            guessed_correct_txt.draw(win)
        else:
            guesses_remain -= 1
            guessed_incorrect_str += curr_guess + " "
            guessed_incorrect.undraw()
            guessed_incorrect = Text(guessed_incorrect_pt, guessed_incorrect_str)
            guessed_incorrect.draw(win)

            if guesses_remain == 5:
                head.draw(win)
            elif guesses_remain == 4:
                body.draw(win)
            elif guesses_remain == 3:
                right_leg.draw(win)
            elif guesses_remain == 2:
                left_leg.draw(win)
            elif guesses_remain == 1:
                right_arm.draw(win)
            elif guesses_remain == 0:
                left_arm.draw(win)

        # win conditions
        if guessed_correct.split(" ") == list(secret_word):
            end_pt = Point(win_width / 2, 25)
            end = Text(end_pt, "winner!")
            end.draw(win)
            win.getMouse()
        elif guesses_remain == 0:
            end_pt = Point(win_width / 2, 25)
            sorry_str = "sorry, you did not win.\n the word was " + secret_word
            end = Text(end_pt, sorry_str)
            end.draw(win)
            win.getMouse()








def play_command_line(secret_word):
    guesses_lst = []
    guesses_remain = 6
    guessed_correct = make_hidden_secret(secret_word, guesses_lst)
    while guesses_remain >= 0 and not guessed_correct == secret_word:
        print("already guessed:", guesses_lst)
        print("guesses remaining:", guesses_remain)
        print(guessed_correct)
        curr_guess = input("guess a letter: ")
        guesses_lst.append(curr_guess)
        if letter_in_secret_word(curr_guess, secret_word):
            guessed_correct = make_hidden_secret(secret_word, guesses_lst)
        else:
            guesses_remain -= 1
        if guessed_correct.split(" ") == list(secret_word):
            print("winner!\n" + guessed_correct)
            break
        elif guesses_remain == 0:
            print("sorry, you did not guess the word.")
            print("the secret word was " + secret_word)
        else:
            print()


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
