"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
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
    iter = 0
    for i in range(1, number + 1):
        iter += i
    return iter

def sum_n_cubes(number):
    pass


def encode_better():
    pass


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
