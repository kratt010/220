"""
Name: Brendan Kratt
lab9.py
"""


def build_board():
    board = []
    for i in range(1, 10):
        board.append(i)
    return board


def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    if board[position-1] == "x" or board[position-1] == "o":
        return False
    return True


def fill_spot(board, position, character):
    new_chr = character.strip().lower()
    board[position] = new_chr


def winning_game(board):
    if board[0] == board[4] == board[8]:  # diagonal top left to btm right
        return True
    if board[6] == board[4] == board[2]:  # diagonal top right to btm left
        return True
    if board[0] == board[3] == board[6]:  # left Vertical
        return True
    if board[1] == board[4] == board[7]:  # mid Vertical
        return True
    if board[2] == board[5] == board[8]:  # right Vertical
        return True
    if board[0] == board[1] == board[2]:  # top Horizontal
        return True
    if board[3] == board[4] == board[5]:  # mid Horizontal
        return True
    if board[6] == board[7] == board[8]:  # bot Horizontal
        return True
    return False


def game_over(board):
    if 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 in board:
        return False
    return True


def get_winner(board):
    if board[0] == board[4] == board[8]:  # diagonal top left to btm right
        if board[0] == "x":
            return "x"
        return "o"
    if board[6] == board[4] == board[2]:  # diagonal top right to btm left
        if board[6] == "x":
            return "x"
        return "o"
    if board[0] == board[3] == board[6]:  # left Vertical
        if board[0] == "x":
            return "x"
        return "o"
    if board[1] == board[4] == board[7]:  # mid Vertical
        if board[1] == "x":
            return "x"
        return "o"
    if board[2] == board[5] == board[8]:  # right Vertical
        if board[2] == "x":
            return "x"
        return "o"
    if board[0] == board[1] == board[2]:  # top Horizontal
        if board[0] == "x":
            return "x"
        return "o"
    if board[3] == board[4] == board[5]:  # mid Horizontal
        if board[3] == "x":
            return "x"
        return "o"
    if board[6] == board[7] == board[8]:  # bot. Horizontal
        if board[6] == "x":
            return "x"
        return "o"


def play(board):
    print_board(board)  # first display of empty board
    while True:  # "game loop," if this broken, game is over.
        turn = "x"
        position = eval(input(turn + "'s, choose a position: "))
        while not is_legal(board, position):  # if input illegal, repeat input until legal
            print_board(board)
            position = eval(input(turn + "'s, choose a position: "))
        board[position-1] = "x"
        print_board(board)

        if game_over(board):  # if game tied, end tied game
            print("tie")
            break
        else:
            if winning_game(board):  # else, check if game won. if so, end won game
                winner = get_winner(board)
                print(winner + "'s win!")
                break

        turn = "o"
        position = eval(input(turn + "'s, choose a position: "))
        while not is_legal(board, position):
            print_board(board)
            position = eval(input(turn + "'s, choose a position: "))
        board[position-1] = "o"
        print_board(board)

        if game_over(board):  # if game tied, end tied game
            print("tie")
            break
        else:
            if winning_game(board):  # else, check if game won. if so, end won game
                winner = get_winner(board)
                print(winner + "'s win!")
                break


def main():
    while True:
        play(build_board())  # contains game, game loop
        play_again = input("play again? ")  # only executes after game loop broken
        if not play_again[0].lower() == "y":
            break


if __name__ == '__main__':
    main()
