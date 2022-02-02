"""
Name: Brendan Kratt
hw4.py

Problem:
Defines three functions that use a graphics package to output drawings and calculations based upon
those drawings. Additionally, a fourth function estimates pi using a loop and the modulus operator.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
from graphics import GraphWin, Point, Text, Rectangle, Circle


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move square
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50, 50), Point(100, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # for num_clicks number of times, create copies of object shape at mouseclick
    for i in range(num_clicks):
        new_shape = shape
        click = win.getMouse()
        center = shape.getCenter()  #
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        new_p1 = Point(new_shape.getP1().getX() + change_x, new_shape.getP1().getY() + change_y)
        new_p2 = Point(new_shape.getP2().getX() + change_x, new_shape.getP2().getY() + change_y)
        Rectangle(new_p1, new_p2).setOutline("red").setFill("red").draw(win)
    Text(Point(200, 200), "Click again to close").draw(win)
    win.getMouse()
    win.close()


def rectangle():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Rectangle", width, height)

    # Gathers two mouse inputs for opposite corners of the rectangle
    point_1 = win.getMouse()
    point_2 = win.getMouse()
    # Draws a green rectangle with corners at point_1 and point_2
    shape = Rectangle(point_1, point_2)
    shape.setFill("Green")
    shape.draw(win)

    # Calculates the length and height of the drawn rectangle
    length_rect = abs(point_1.getX() - point_2.getX())
    height_rect = abs(point_1.getY()-point_2.getY())

    # Calculates the perimeter and area
    perim_str_val = str(2 * length_rect + 2 * height_rect)
    area_str_val = str(length_rect * height_rect)

    # Displays calculated perimeter and area
    perim_txt_pt = Point(width / 2, height - 50)
    area_txt_pt = Point(width / 2, height - 25)
    Text(perim_txt_pt, "Perimeter: " + perim_str_val).draw(win)
    Text(area_txt_pt, "Area: " + area_str_val).draw(win)

    # Displays text, waits for mouse input, then closes when received
    Text(Point(200, 200), "Click again to close").draw(win)
    win.getMouse()
    win.close()


def circle():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Circle", width, height)

    # Gathers mouse input for center and circumference
    point_center = win.getMouse()
    point_circumference = win.getMouse()

    # calculates the difference between x and y and then squares them
    x_diff_sqr = (point_circumference.getX() - point_center.getX()) ** 2
    y_diff_sqr = (point_circumference.getY() - point_center.getY()) ** 2

    # Finished calculation with the square root of the sums
    radius = math.sqrt(x_diff_sqr + y_diff_sqr)

    # Draws the circle based on previous information
    circ = Circle(point_center, radius)
    circ.setFill("Light Blue")
    circ.draw(win)

    # Writes text on screen
    rad_txt_pt = Point(width / 2, height - 25)
    Text(rad_txt_pt, "Radius: " + str(radius)).draw(win)
    Text(Point(200, 200), "Click again to close").draw(win)

    # Waits for input, after received closes
    win.getMouse()
    win.close()

def pi2():
    num_terms = eval(input("enter the number of terms to sum: "))
    pi_val = 0
    denom_val = 1
    for i in range(1, num_terms + 1):
        neg_pos = (-1 + 2 * (i % 2))  # if i odd, neg_pos = +1 . Even, -1.
        pi_val += 4 * neg_pos / denom_val
        denom_val += 2
    print("pi approximation:", pi_val)
    print("accuracy:", abs(math.pi - pi_val))


if __name__ == '__main__':
    pass
