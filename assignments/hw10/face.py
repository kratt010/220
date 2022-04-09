from graphics import *


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        mouth_center_x = self.mouth.getCenter().getX()
        # mouth_off offsets apex of the triangle halfway between self.mouth and self.head edge
        mouth_off = abs(self.mouth.getCenter().getY() - self.head.getCenter().getY()) / 2
        apex_pt = Point(mouth_center_x, self.mouth.getCenter().getY() + mouth_off)

        left_line_p1 = self.mouth.getP1()
        right_line_p1 = self.mouth.getP2()
        self.left_smile_line = Line(left_line_p1, apex_pt)
        self.right_smile_line = Line(right_line_p1, apex_pt)
        self.left_smile_line.draw(self.window)
        self.right_smile_line.draw(self.window)

    def shock(self):
        center = self.mouth.getCenter()
        radius = self.left_eye.getRadius()  # either eye works, same radius
        shock_mouth = Circle(center, radius)
        self.mouth.undraw()
        shock_mouth.draw(self.window)

    def wink(self):
        center_x = self.left_eye.getCenter().getX()
        center_y = self.left_eye.getCenter().getY()
        radius = self.left_eye.getRadius()
        self.left_eye.undraw()
        line_p1 = Point(center_x - radius, center_y)
        line_p2 = Point(center_x + radius, center_y)
        self.left_eye = Line(line_p1, line_p2)
        self.left_eye.draw(self.window)


win_width = 400
win_height = 400
win = GraphWin("Face", win_width, win_height)
center_pt = Point(win_width/2, win_height/2)
x = Face(win, center_pt, 150)
win.getMouse()
x.shock()
win.getMouse()
