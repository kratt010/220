from graphics import *
win = GraphWin("My  Rect", 100, 100)
x = Rectangle(Point(0, 0), Point(25, 25))
x.draw(win)
win.getMouse()
win.close()
