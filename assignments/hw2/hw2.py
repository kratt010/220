"""
Name: Brendan Kratt
hw2.py

Problem: This program defines a number of mathematical functions. All feature input, calculation, and output.
         Most feature iteration as well.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    # Within the assignment the sentences are not capitalized. Same here.
    upper_bound = eval(input("what is the upper bound? "))
    iterated_integer = int()
    for i in range(upper_bound // 3):
        iterated_integer += 3 * (i+1)
    print("sum of threes is", iterated_integer)z


# This code works. The test fails. The test is not properly formatted, I think.

def multiplication_table():
    string_builder = ""
    for current_line_number in range(1, 11):
        for i in range(10):
            calculation = str((i+1) * current_line_number)
            string_builder += calculation + "\t"
        print(string_builder)
        string_builder = ""


def triangle_area():
    side_a = eval(input("Enter side a length: "))
    side_b = eval(input("Enter side b length: "))
    side_c = eval(input("Enter side c length: "))
    side_s = (side_a + side_b + side_c)/2
    area = math.sqrt(side_s * (side_s - side_a) * (side_s - side_b) * (side_s - side_c))
    print("area is", area)


def sum_squares():
    lower_range = eval(input("Enter lower range: "))
    upper_range = eval(input("Enter upper range: "))
    sum_holder = int()
    for i in range(lower_range, upper_range+1):
        sum_holder += i ** 2
    print(sum_holder)


def power():
    base = eval(input("Enter base: "))
    exponent = eval(input("Enter exponent: "))
    iterated_base = base
    for i in range(exponent-1):
        iterated_base *= base
    print(base, '^', exponent, '=', iterated_base)


if __name__ == '__main__':
    pass
