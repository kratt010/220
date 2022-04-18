def find_and_remove_first(lst, value):
    pos = lst.index(value)  # this is the best method to use, does not necessitate while loop
    lst[pos] = "Brendan"


def read_data(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    count = 0
    while count < len(lines):
        lines[count] = lines[count].strip()
        count += 1

    one_large_line = " ".join(lines)
    formatted_lst = one_large_line.split(" ")
    return formatted_lst


def is_in_linear(search_val, values):
    count = 0
    while count < len(values):
        if values[count] == search_val:
            return True
        count += 1
    return False


def good_input():
    while True:
        num = eval(input("Enter a number between 1 and 10: "))
        if 1 <= num <= 10:
            return num
        else:
            print("Input was outside the expected range. Try again.")


def num_digits():
    num = 1
    while num > 0:
        num = eval(input("Enter a positive integer: "))
        test_num_val = num
        digits = 0
        while test_num_val > 0:
            test_num_val = test_num_val // 10
            digits += 1
        if num > 0:
            print("Number of digits:", digits)


def hi_lo_game():
    from random import randint

    random_num = randint(1, 100)
    tries = 0
    won = False
    while tries < 7 and won is False:
        guess = eval(input("Guess the number: "))
        if random_num > guess:
            print("Too low.")
        if random_num < guess:
            print("Too high.")
        if random_num == guess:
            print("Correct!")
            won = True
        tries += 1
    if won is True:
        print("You win in", tries, "guesses!")
    if won is False:
        print("Sorry, you lose. The number was " + str(random_num) + ".")
