import math
from graphics import GraphWin, Circle, Text, Point, time, color_rgb
from random import randint


def get_random(move_amount):
    return randint(-move_amount, move_amount)


def did_collide(ball, ball2):
    ball1_cent = ball.getCenter()
    ball2_cent = ball2.getCenter()

    ball1_x = ball1_cent.getX()
    ball1_y = ball1_cent.getY()
    ball2_x = ball2_cent.getX()
    ball2_y = ball2_cent.getY()
    term_1 = (ball1_x - ball2_x) ** 2
    term_2 = (ball1_y - ball2_y) ** 2
    distance = math.sqrt(term_1 + term_2)
    if distance < 50:
        return True
    return False


def hit_vertical(ball, win):
    ball_cent = ball.getCenter()
    ball_x = ball_cent.getX()
    if ball_x >= win.getWidth() - 25 or ball_x <= 25:
        return True
    return False


def hit_horizontal(ball, win):
    ball_cent = ball.getCenter()
    ball_y = ball_cent.getY()
    if ball_y >= win.getHeight() - 25 or ball_y <= 25:
        return True
    return False


def get_random_color():
    return color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))



win_width = 400
win_height = 400
win = GraphWin("Bumper Cars", win_width, win_height)
win.setBackground("white")

close_pt = Point(win_width/2, win_height/2)
close_txt = Text(close_pt, "Click anywhere to close.")
close_txt.draw(win)

circle_rad = 25

car_1_pt = Point(win_width/4, win_height/2)
car_1 = Circle(car_1_pt, circle_rad)
car_1.setFill(get_random_color())
car_1.draw(win)

car_2_pt = Point(win_width*3/4, win_height/2)
car_2 = Circle(car_2_pt, circle_rad)
car_2.setFill(get_random_color())
car_2.draw(win)

car1_move_x = get_random(10)
car1_move_y = get_random(10)
car2_move_x = get_random(10)
car2_move_y = get_random(10)

while True:
    time.sleep(0.1)  # loop cycles 10x a second, roughly

    if hit_horizontal(car_1, win):
        car1_move_y = -car1_move_y  # reverse Y direction
        car_1.move(car1_move_x, car1_move_y)  # these functions, wonky themselves, fix a wonky bug

    if hit_vertical(car_1, win):
        car1_move_x = -car1_move_x
        car_1.move(car1_move_x, car1_move_y)

    if hit_horizontal(car_2, win):
        car2_move_y = -car2_move_y  # reverse Y direction
        car_2.move(car2_move_x, car2_move_y)
    if hit_vertical(car_2, win):
        car2_move_x = -car2_move_x  # reverse X direction
        car_2.move(car2_move_x, car2_move_y)

    if did_collide(car_1, car_2):
        car_1_move_x = -car1_move_x # reverse X & Y directions of both
        car1_move_y = -car1_move_y
        car_2_move_x = -car2_move_x
        car2_move_y = -car2_move_y

        car_1.move(car1_move_x, car1_move_y)  # they have an affinity/magnetism toward each other
        car_2.move(car2_move_x, car2_move_y)  # attempts to stop that spiral, not always well

    car_1.move(car1_move_x, car1_move_y)
    car_1.undraw()
    car_1.draw(win)

    car_2.move(car2_move_x, car2_move_y)
    car_2.undraw()
    car_2.draw(win)  # moves by set amount, updates on screen
    if not win.checkMouse() is None:  # ends on mouse input
        break
