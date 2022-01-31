"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

from graphics import *


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

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        new_shape = shape
        click = win.getMouse()
        center = shape.getCenter()  # center of circle
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
    win = GraphWin("Clicks", width, height)
    point_1 = win.getMouse()
    point_2 = win.getMouse()
    shape = Rectangle(point_1, point_2)
    shape.setFill("Green")
    shape.draw(win)
    length_rect = abs(point_1.getX() - point_2.getX())
    height_rect = abs(point_1.getY()-point_2.getY())
    perim_str_val = str(2 * length_rect + 2 * height_rect)
    area_str_val = str(length_rect * height_rect)
    perim_txt_pt = Point(width / 2, height - 50)
    area_txt_pt = Point(width / 2, height - 25)
    Text(perim_txt_pt, "Perimeter: " + perim_str_val).draw(win)
    Text(area_txt_pt, "Area: " + area_str_val).draw(win)
    Text(Point(200, 200), "Click again to close").draw(win)
    win.getMouse()
    win.close()


def circle():
    pass


def pi2():
    pass


if __name__ == '__main__':
    pass
