"""
Name: Brendan Kratt
hw6.py

Problem: This program defines a number of functions, some relating to string and list methods,
         others touching onto with the return statement.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from math import pi


def cash_converter():
    num_input = eval(input("enter an integer: "))
    print("That is ${:.2f})".format(num_input))


def encode():
    lst_chrs = list(input("enter a message: "))
    key = eval(input("enter a key: "))
    conv_lst = []
    for i in lst_chrs:
        conv_lst.append(chr(ord(i) + key))
    print("".join(conv_lst))


def sphere_area(radius):
    area = 4 * pi * radius ** 2
    return area


def sphere_volume(radius):
    vol = 4/3 * pi * radius ** 3
    return vol


def sum_n(number):
    sum_output = 0
    for i in range(1, number + 1):
        sum_output += i
    return sum_output


def sum_n_cubes(number):
    cube_output = 0
    for i in range(1, number + 1):
        cube_output += i ** 3
    return cube_output


def encode_better():
    text_input = input("Text: ")
    key_input = input("Key: ") * len(text_input)
    lst_key_ord = []
    lst_txt_ord = []

    # ordinal list of key input
    for i in key_input:
        lst_key_ord.append(ord(i) - 65)

    # ordinal list of text input
    for i in text_input:
        lst_txt_ord.append(ord(i) - 65)

    # unformatted addition of ordinals
    lst_shifted_ord = []
    for i in range(len(lst_txt_ord)):
        lst_shifted_ord.append(lst_txt_ord[i] + lst_key_ord[i])

    # formats ordinals
    final_ord_lst = []
    for i in range(len(lst_shifted_ord)):
        conv_ord = lst_shifted_ord[i] % 58
        final_ord_lst.append(conv_ord)

    # prepares, prints output
    iter_output = ""
    for i in final_ord_lst:
        iter_output += chr(i + 65)
    print(iter_output)



if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
