import algorithms


def main():
    # Tests find_and_remove_first
    print("find_and_remove_first: ")
    lst = [1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9, 10]
    value = 7
    print(lst)
    algorithms.find_and_remove_first(lst, value)
    print(lst)
    print()

    # Tests read_data
    print("Read_data:")
    file_name = "data_sorted.txt"

    file = open(file_name, "r")
    print(file.readlines())
    file.close()

    print(algorithms.read_data(file_name))
    print()

    # Tests is_in_linear
    print("Is_in_linear:")
    lst = [1, 2, 3, 4, 5, 999, 10, -2, 59, 14]
    first = -99
    second = 999

    is_first_in_lst = str(algorithms.is_in_linear(first, lst))
    is_second_in_lst = str(algorithms.is_in_linear(second, lst))
    print(lst)
    print(str(first) + " in list: " + is_first_in_lst)
    print(str(second) + " in list: " + is_second_in_lst)
    print()

    # Tests good_input
    print("Good_input:")
    algorithms.good_input()
    print("Input accepted.")
    print()

    # Tests num_digits
    print("Num_digits:")
    print("Enter num <= 0 to end.")
    algorithms.num_digits()
    print()

    # Tests hi_lo_game
    print("Hi_lo_game:")
    play_again = True
    while play_again is True:
        algorithms.hi_lo_game()
        ask_play_again = input("Play again? Y/N ").lower()
        if ask_play_again[0] == "n":
            play_again = False
        print()
    print("Tests concluded.")


main()
