"""
Name: Brendan Kratt
hw3.py

Problem: This program defines a variety of situational functions. All functions take input,
         store values, perform some sort of calculation, and then release an output.
         Some functions are mathematical, some are related to work uses, however all utilize
         the for loop.


Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    num_grades = eval(input("how many grades will you enter? "))
    grades_sum = 0.0
    for i in range(num_grades):
        grades_sum += eval(input("Enter grade: "))
    print("average is", grades_sum / num_grades)


def tip_jar():
    tip_bal = 0.0
    for i in range(5):
        tip_bal += eval(input("how much would you like to donate? "))
    print("total tips:", tip_bal)


def newton():
    orig_radicand = eval(input("What number do you want to square root? "))
    iter_amt = eval(input("How many times should we improve the approximation? "))
    working_approx = orig_radicand
    for i in range(iter_amt):
        working_approx = (working_approx + orig_radicand / working_approx) / 2
    print("the square root is approximately", working_approx)


def sequence():
    num_terms = eval(input("how many terms would you like? "))
    seq_iter_val = ''
    for i in range(1, num_terms+1):
        seq_iter_val += str(i - (1 - i % 2)) + ' '  # If i even, equals i minus 1. Odd, equals i.
    print(seq_iter_val)


def pi():
    num_terms = eval(input("how many terms in the series? "))
    iter_val_pi = 2  # initial value 2, since the given equation was for pi/2, not pi
    for i in range(2, num_terms+2):
        denom_value = i - (1 - i % 2)  # if i even, denom_values equals i minus 1. Else, equals i.
        num_value = i - (i % 2)        # If i odd, num_value equals i minus 1. Else, equals i.
        iter_val_pi *= (num_value/denom_value)
    print(iter_val_pi)


if __name__ == '__main__':
    pass
