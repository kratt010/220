"""
Name: Brendan Kratt
hw3.py

Problem: <Brief description of the problem that this program solves>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    num_grades = eval(input("how many grades will you enter? "))
    grades_lst = []
    for i in range(num_grades):
        grades_lst.append(eval(input("Enter grade: ")))
    print("average is", (sum(grades_lst) / len(grades_lst)))


def tip_jar():
    tip_bal = []
    for i in range(5):
        tip_bal.append(eval(input("how much would you like to donate? ")))
    print("total tips:", sum(tip_bal))


def newton():
    radicand = eval(input("What number do you want to square root? "))
    iterations = eval(input("How many times should we improve the approximation? "))
    approx = radicand
    for i in range(iterations):
        approx = (approx+radicand/approx)/2
    print("the square root is approximately", approx)


def sequence():
    num_terms = eval(input("how many terms would you like? "))
    for i in range(1, num_terms+1):
        print(i - (1 - i % 2))  # If i even, print i minus 1. Odd, print i.


def pi():
    list_terms = []
    num_terms = eval(input("how many terms in the series? "))
    for i in range(2, num_terms+2):
        denom_value = i - (1 - i % 2)  # if i even, denom_values equals i minus 1. Else, equals i.
        num_value = i - (i % 2)  # If i odd, num_value equals i minus 1. Else, equals i.
        list_terms.append(num_value/denom_value)
    pi_value = 1
    for term in list_terms:
        pi_value *= term
    print(pi_value * 2)


if __name__ == '__main__':
    pass
