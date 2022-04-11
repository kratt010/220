from labs.lab10.door import Door
from labs.lab10.button import Button
from graphics import GraphWin, Point, Rectangle, Text, Line
from random import randint

# defines window
win_width = 425
win_height = 425
win = GraphWin("Three Door Game", win_width, win_height)
win.setBackground("steel blue")

# defines rectangles for doors
rect_1_p1 = Point(50, 100)
rect_1_p2 = Point(125, 300)
rect_1 = Rectangle(rect_1_p1, rect_1_p2)

rect_2_p1 = Point(175, 100)
rect_2_p2 = Point(250, 300)
rect_2 = Rectangle(rect_2_p1, rect_2_p2)

rect_3_p1 = Point(300, 100)
rect_3_p2 = Point(375, 300)
rect_3 = Rectangle(rect_3_p1, rect_3_p2)

# defines, colors, draws doors
door_1 = Door(rect_1, "Door 1")
door_1.color_door("saddle brown")
door_1.draw(win)

door_2 = Door(rect_2, "Door 2")
door_2.color_door("saddle brown")
door_2.draw(win)

door_3 = Door(rect_3, "Door 3")
door_3.color_door("saddle brown")
door_3.draw(win)

# defines, draws scores and score box
score_box_p1 = Point(25, 25)
score_box_p2 = Point(125,75)
score_box = Rectangle(score_box_p1, score_box_p2)
score_box.draw(win)

dividing_line = Line(Point(75, 25), Point(75, 75))
dividing_line.draw(win)

won_label_pt = Point(50, 18)
won_label = Text(won_label_pt, "wins")
won_label.draw(win)

lost_label_pt = Point(102, 18)
lost_label = Text(lost_label_pt, "losses")
lost_label.draw(win)

score_won_pos = Point(50, 50)
score_won = Text(score_won_pos, "0")
score_won.draw(win)

score_lost_pos = Point(100, 50)
score_lost = Text(score_lost_pos, "0")
score_lost.draw(win)

# defines, draws quit box
button_p1 = Point(400, 25)
button_p2 = Point(300, 75)
button_rect = Rectangle(button_p1, button_p2)
quit_box = Button(button_rect, "Quit")
quit_box.draw(win)

# defines, draws text items
game_txt_pt = Point(win_width/2, 50)
game_txt = Text(game_txt_pt, "I have a secret door")
game_txt.draw(win)

help_txt_pt = game_txt_pt.clone()
help_txt_pt.move(0, 300)
help_txt = Text(help_txt_pt, "Click to guess which is the secret door!")
help_txt.draw(win)


def won():
    game_txt.setText("you win!")
    help_txt.setText("click anywhere to play again")
    score_won.setText(str(eval(score_won.getText()) + 1))


def lost():
    game_txt.setText("sorry, incorrect!")
    help_txt.setText("click anywhere to play again")
    score_lost.setText(str(eval(score_lost.getText()) + 1))
    if secret_door == 1:
        door_1.color_door("green")
    if secret_door == 2:
        door_2.color_door("green")
    if secret_door == 3:
        door_3.color_door("green")


# resets needed items to default state
def reset():
    door_1.color_door("saddle brown")
    door_2.color_door("saddle brown")
    door_3.color_door("saddle brown")
    door_1.set_secret(False)
    door_2.set_secret(False)
    door_3.set_secret(False)
    game_txt.setText("I have a secret door")
    help_txt.setText("Click to guess which is the secret door!")


while True:  # loops unless broken
    reset()  # for each loop reset to original state

    # determines secret door for round
    secret_door = randint(1, 3)
    if secret_door == 1:
        door_1.set_secret(True)
    elif secret_door == 2:
        door_2.set_secret(True)
    elif secret_door == 3:
        door_3.set_secret(True)

    # game logic
    click_pt = win.getMouse()  # begins round with choice

    if quit_box.is_clicked(click_pt):  # quit button clicked, end program
        break
    elif door_1.is_clicked(click_pt):  # door 1 clicked. if secret, won. else, lost.
        if door_1.is_secret():
            door_1.color_door("green")
            won()
        else:
            door_1.color_door("red")
            lost()
    elif door_2.is_clicked(click_pt):  # door 2 clicked. if secret, won. else, lost.
        if door_2.is_secret():
            door_2.color_door("green")
            won()
        else:
            door_2.color_door("red")
            lost()
    elif door_3.is_clicked(click_pt):  # door 3 clicked. if secret, won. else, lost.
        if door_3.is_secret():
            door_3.color_door("green")
            won()
        else:
            door_3.color_door("red")
            lost()
    click_pt_2 = win.getMouse()  # click for "click to continue"
    if quit_box.is_clicked(click_pt_2):  # if above click on quit button, quit
        break


