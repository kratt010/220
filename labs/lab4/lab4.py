from graphics import *

width = 400
height = 400
win = GraphWin("Happy Valentines Day!", width, height)
win.setBackground("Pink")

msg_pt = Point(width/2, height - 100)
msg_txt = "Happy Valentines Day!"
msg = Text(msg_pt, msg_txt)
msg.draw(win)

# Convoluted system here. Offset == distance from center to draw each pt on rotated square (Polygon)

sqr_corner_offset = 50
top_pt_sqr = Point(width / 2, height / 2 - sqr_corner_offset)
left_pt_sqr = Point(width / 2 - sqr_corner_offset, height / 2)
right_pt_sqr = Point(width / 2 + sqr_corner_offset, height / 2)
btm_pt_sqr = Point(width / 2, height / 2 + sqr_corner_offset)

# Draws a square rotated 45 degrees at the center of the window
heart_sqr = Polygon(top_pt_sqr, left_pt_sqr, btm_pt_sqr, right_pt_sqr)
heart_sqr.setFill("Red")
heart_sqr.setOutline("Red")
heart_sqr.draw(win)

# gets center of left line, then uses that as center of circle.
left_line = Line(left_pt_sqr, top_pt_sqr)
left_line.draw(win)
# Calculates line length, since its length / 2 is the radius of both circ1 and circ2
circ1_center = left_line.getCenter()
circ1 = Circle(circ1_center, 35.35)  # 35.35 == result of external Pythagorean theorem calculation.
circ1.setFill("Red")
circ1.setOutline("Red")
circ1.draw(win)

# Same as above
right_line = Line(right_pt_sqr, top_pt_sqr)
circ2_center = right_line.getCenter()
circ2 = Circle(circ2_center, 35.35)
circ2.setFill("Red")
circ2.setOutline("Red")
circ2.draw(win)

# All drawn below create the arrow.
arrow_x = 0
arrow_y = 400
arrow_p1 = Point(arrow_x - 150, arrow_y + 150)
arrow_p2 = Point(arrow_x, arrow_y)
arrow_body = Line(arrow_p1, arrow_p2)
arrow_body.setArrow("last")

time.sleep(1)


for i in range(57): # moves, loops, and updates the arrow
    time.sleep(0.01)
    arrow_body.undraw()
    arrow_body.draw(win)
    arrow_body.move(5, -5)

time.sleep(0.25)
msg.undraw()
msg_txt = "Click anywhere to close!"
msg = Text(msg_pt, msg_txt)
msg.draw(win)

win.getMouse()
win.close()
