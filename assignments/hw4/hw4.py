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

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move circle")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(100,100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    new_shape = shape
    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):

        click = win.getMouse()
        center = shape.getCenter()  # center of circle
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        new_p1 = Point(new_shape.getP1().getX() - change_x, new_shape.getP1().getY() - change_y)
        new_p2 = Point(new_shape.getP2().getX() - change_x, new_shape.getP2().getY()- change_y)
        new_shape = Rectangle(new_p1, new_p2)
        new_shape.setOutline("red")
        new_shape.setFill("red")
        new_shape.draw(win)

    win.getMouse()
    win.close()
squares()

def rectangle():
    pass


def circle():
    pass


def pi2():
    pass


if __name__ == '__main__':
    pass
