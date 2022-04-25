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

# lab 13


def is_in_binary(search_val, values):
    # binary search assumed a sorted list, so we utilize that.
    low_pos = 0
    high_pos = len(values) - 1
    while low_pos <= high_pos:
        middle = (low_pos + high_pos) // 2
        if search_val == values[middle]:
            return True
        elif search_val > values[middle]:
            low_pos = middle + 1
        else:
            high_pos = middle - 1
    return False


def selection_sort(values):
    len_lst = len(values)
    for i in range(len_lst):
        lowest_pos = i  # assumes current position is position of lowest val
        for g in range(i + 1, len_lst):
            if values[lowest_pos] > values[g]:  # if assumption invalidated, change value to new pos
                lowest_pos = g

        # if value changed from assumption, swap positions.
        # else, do nothing.
        if not lowest_pos == i:
            placeholder = values[i]
            values[i] = values[lowest_pos]
            values[lowest_pos] = placeholder
    return values


def calc_area(rect):
    # abs. value lets us sidestep the failure case that arises if p1 and p2 are out of order.
    length = abs(rect.getP1().getX() - rect.getP2().getX())
    height = abs(rect.getP1().getY() - rect.getP2().getY())
    area = length * height
    return area


def rect_sort(rectangles):
    lst_areas = []
    for rect in rectangles:
        area = calc_area(rect)
        lst_areas.append(area)  # pos of rect on original list == pos of area on new list
    # defines dictionary. key == area, value == rectangle
    my_dict = dict(zip(lst_areas, rectangles))
    sorted_areas = selection_sort(lst_areas)
    sorted_rectangles = []
    for value in sorted_areas:
        sorted_rectangles.append(my_dict[value])
    return sorted_rectangles
