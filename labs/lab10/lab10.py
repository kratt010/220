from graphics import GraphWin, Point, Rectangle
from door import Door
from button import Button

win_width = 400
win_height = 400
win = GraphWin("Door", win_width, win_height)
win.setBackground("gray")

button_p1 = Point(150, 25)
button_p2 = Point(250, 125)
button_rect = Rectangle(button_p1, button_p2)
my_button = Button(button_rect, "Exit")
my_button.draw(win)

door_p1 = Point(125, 400)
door_p2 = Point(275, 150)
door_rect = Rectangle(door_p1, door_p2)
my_door = Door(door_rect, "")
my_door.draw(win)
my_door.close("maroon", "Closed")


while True:
    x = win.getMouse()
    if my_button.is_clicked(x):
        break
    elif my_door.is_clicked(x):
        my_door.open("white", "Open")
    x = win.getMouse()
    if my_button.is_clicked(x):
        break
    elif my_door.is_clicked(x):
        my_door.close("maroon", "Closed")