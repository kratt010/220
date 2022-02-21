from graphics import Entry, Text, GraphWin, Point, Circle, Polygon, color_rgb, update
import math


# I defined this function. It greatly simplifies triangle()
def distance_calc(dx, dy):
    length = math.sqrt(dx*dx + dy*dy)
    return length


def triangle():
    # defines window
    win_width = 400
    win_height = 400
    win = GraphWin("Triangle", win_width, win_height)
    win.setBackground("white")

    # collects mouse input, assigns X and Y of each to variables
    m1 = win.getMouse()
    m2 = win.getMouse()
    m3 = win.getMouse()
    m1_x = m1.getX()
    m1_y = m1.getY()
    m2_x = m2.getX()
    m2_y = m2.getY()
    m3_x = m3.getX()
    m3_y = m3.getY()

    # calculates perimeter, area
    dx1 = m1_x - m2_x
    dy1 = m1_x - m2_x
    dx2 = m1_x - m3_x
    dy2 = m1_y - m3_y
    dx3 = m3_x - m2_x
    dy3 = m3_y - m2_y
    a = distance_calc(dx1, dy1)
    b = distance_calc(dx2, dy2)
    c = distance_calc(dx3, dy3)
    perim = a + b + c
    s = perim / 2
    area = math.sqrt(abs(s * (s-a) * (s-b) * (s-c)))  # The abs. solves a quirk of the calculation.

    # draws triangle
    triang = Polygon(m1,m2,m3)
    triang.draw(win)

    # draws perimeter
    perim_pt = Point(win_width/2, win_height - 100)
    perim_text = Text(perim_pt, "Perimeter: " + str(perim))
    perim_text.draw(win)

    # drwas area
    area_pt = Point(win_width/2, win_height - 50)
    area_text = Text(area_pt, "Area: " + str(area))
    area_text.draw(win)

    # Waits for mouse input to close
    close_pt = Point(win_width/2, win_height - 25)
    close_text = Text(close_pt, "Click anywhere to close.")
    close_text.draw(win)
    win.getMouse()



def color_shape():

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # red_entry_pt is 50 pixels to the right of red_text_pt
    red_entry_pt = red_text_pt.clone()
    red_entry_pt.move(50,0)
    red_entry = Entry(red_entry_pt, 3)
    red_entry.draw(win)
    # green_entry_pt is 30 pixels down from red
    green_entry_pt = red_entry_pt.clone()
    green_entry_pt.move(0, 30)
    green_entry = Entry(green_entry_pt, 3)
    green_entry.draw(win)
    # blue_entry_pt is 30 pixels down from green
    blue_entry_pt = green_entry_pt.clone()
    blue_entry_pt.move(0, 30)
    blue_entry = Entry(blue_entry_pt, 3)
    blue_entry.draw(win)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    # updates color on mouse input five total times
    for i in range(5):
        win.getMouse()
        specified_red = int(red_entry.getText())
        specified_green = int(green_entry.getText())
        specified_blue = int(blue_entry.getText())
        specified_color = color_rgb(specified_red, specified_green, specified_blue)
        shape.setFill(specified_color)

    # Wait for another click to exit, displays text saying as such
    close_pt = Point(win_width / 2, win_height - 50)
    close_text = Text(close_pt, "Click anywhere to close.")
    close_text.draw(win)

    win.getMouse()
    win.close()


def process_string():
    string1 = input("Enter a string: ")
    len_string = len(string1)
    print(string1[0])
    print(string1[-1])
    print(string1[2:5])
    print(string1[0] + string1[-1])
    print(string1[0] * 3)
    for i in range(10):
        print(string1[0:3], end="")
    print()
    for i in range(len_string):
        print(string1[i])
    print(len_string)

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = [values[2], values[3], values[-2]]
    print(x)
    x = [values[2], values[-3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[-1])]
    print(x)
    x = values[0] + values[2] + float(values[-1])
    print(x)
    x = len(values)
    print(x)

def another_series():
    series_1 = [2,4,6]
    series_2 = []
    num_terms = eval(input("Enter number of terms to sum: "))
    for i in range(math.ceil(num_terms / len(series_1))):
        series_2.extend(series_1)
    counter = 0
    series_output_str =  ""
    for i in range(num_terms):
        series_output_str += str(series_2[i]) + " "
        counter += series_2[i]
    print(series_output_str)
    print("sum =", counter)

def target():
    # sets up a square window
    win_width = 250
    win_height = 250
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # defines a common center point of all circles
    circles_pt = Point(win_width/2, win_height/2)

    # defines, colors, and draws all circles
    circ_white = Circle(circles_pt, 125)
    circ_white.setFill("white")
    circ_white.draw(win)
    circ_black = Circle(circles_pt, 100)
    circ_black.setFill("black")
    circ_black.draw(win)
    circ_blue = Circle(circles_pt, 75)
    circ_blue.setFill("blue")
    circ_blue.draw(win)
    circ_red = Circle(circles_pt, 50)
    circ_red.setFill("red")
    circ_red.draw(win)
    circ_yellow = Circle(circles_pt, 25)
    circ_yellow.setFill("yellow")
    circ_yellow.draw(win)
    win.getMouse()

