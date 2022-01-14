"""
Name: Brendan Kratt
hw1.py

Problem:
This program defines a variety of simple mathematical functions.
Common among the problems is that all functions accept an input,
evaluate them into a calculable form, perform calculations upon the inputs,
and then print the result to the user.


Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    total_shots = eval(input("Enter the player's total shots: "))
    made_shots = eval(input("Enter how many shots the player made: "))
    percent_shots_made_str = str(100*(made_shots/total_shots)) + '%'
    print("Shooting Percentage: ", percent_shots_made_str)


def coffee():
    pounds_wanted = eval(input("How many pounds of coffee would you like? "))
    total_cost = 10.50 * pounds_wanted + 0.86 * pounds_wanted + 1.50
    print("You're total is: ", total_cost)


def kilometers_to_miles():
    km_input = eval(input("How many kilometers did you travel? "))
    in_miles = km_input / 1.61
    print("That's", in_miles, "miles!")


if __name__ == '__main__':
    pass
