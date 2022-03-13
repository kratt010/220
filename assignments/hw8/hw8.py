"""
Name: Brendan Kratt
hw8.py

Problem: This program defines various functions dealing with return statements and conditionals.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math
from graphics import GraphWin, Text, Circle, Point


def add_ten(nums):
    lst = []
    for i in nums:
        lst.append(i+10)
    nums.clear()
    for i in lst:
        nums.append(i)


def square_each(nums):
    lst = []
    for i in nums:
        lst.append(i * i)
    nums.clear()
    for i in lst:
        nums.append(i)


def sum_list(nums):
    return sum(nums)


def to_numbers(nums):
    nums_calculable = []
    for i in nums:
        nums_calculable.append(eval(i))
    nums.clear()
    for i in nums_calculable:
        nums.append(i)


def sum_of_squares(nums):
    output_lst = []
    for i in nums:
        iter_var = i.split(", ")
        to_numbers(iter_var)
        square_each(iter_var)
        iter_var = sum_list(iter_var)
        output_lst.append(iter_var)
    return output_lst


def starter(weight, wins):
    if wins > 20:
        return True
    if weight > 199:
        return True
    if weight >= 150:
        if weight < 160:
            if wins >= 5:
                return True
    return False


def leap_year(year):
    if year % 100 == 0:
        return bool(year % 400 == 0)
    if year % 4 == 0:
        return True
    return False


def did_overlap(circle_one, circle_two):
    center_1 = circle_one.getCenter()
    center_2 = circle_two.getCenter()
    x_component = (center_2.getX() - center_1.getX()) ** 2
    y_component = (center_2.getY() - center_1.getY()) ** 2
    distance_btwn_centers = math.sqrt(x_component + y_component)

    sum_radii = circle_one.getRadius() + circle_two.getRadius()

    if distance_btwn_centers > sum_radii:
        return False
    return True


def circle_overlap():  # "Too many locals," but can only comply with coding norms with that many.
    # defines window
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    # defines, draws circle1
    center_1 = win.getMouse()
    circumference_point_1 = win.getMouse()
    radius_1 = math.sqrt(  # This line is too long, but I wasn't the one who wrote it.
        (center_1.getX() - circumference_point_1.getX()) ** 2 + (center_1.getY() - circumference_point_1.getY()) ** 2)
    circle_1 = Circle(center_1, radius_1)
    circle_1.setFill("light blue")
    circle_1.draw(win)

    # defines, draws circle2
    center_2 = win.getMouse()
    circumference_point_2 = win.getMouse()
    radius_2 = math.sqrt(                   # ^^ See above
        (center_2.getX() - circumference_point_2.getX()) ** 2 + (center_2.getY() - circumference_point_2.getY()) ** 2)
    circle_2 = Circle(center_2, radius_2)
    circle_2.setFill("light green")
    circle_2.draw(win)

    # defines, draws determ textbox

    bool_val = did_overlap(circle_1, circle_2)
    if bool_val is False:
        determ_msg = "The circles do not overlap"
    else:
        determ_msg = "The circles overlap"

    determ_txt_pt = Point(width/2, height/3)
    determ_txt = Text(determ_txt_pt, determ_msg)
    determ_txt.draw(win)

    # defines, draws closing message
    close_pt = Point(width/2, height/4)
    close_txt = Text(close_pt, "Click again to close")
    close_txt.draw(win)
    win.getMouse()


if __name__ == '__main__':
    pass
