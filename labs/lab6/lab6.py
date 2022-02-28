from graphics import *

# defines window
win_width = 400
win_height = 300
win = GraphWin("Vigenere", win_width, win_height)
win.setBackground("white")

msg_pt = Point(100, 50)
msg_label = Text(msg_pt, "Message to code")
msg_label.draw(win)

keywrd_pt = Point(100, 100)
keywrd_label =  Text(keywrd_pt, "Enter keyword")
keywrd_label.draw(win)

msg_entry_pt = Point(275, 50)
msg_entry = Entry(msg_entry_pt, 20)
msg_entry.draw(win)

keywrd_entry_pt = Point(275, 100)
keywrd_entry = Entry(keywrd_entry_pt, 20)
keywrd_entry.draw(win)

encode_box_p1 = Point(win_width/2 - 50, win_height/2 + 25)
encode_box_p2 = Point(win_width/2 + 50, win_height/2 - 25)
encode_box = Rectangle(encode_box_p1, encode_box_p2)
encode_box.draw(win)

box_txt_pt = encode_box.getCenter()
box_txt = Text(box_txt_pt, "Encode")
box_txt.draw(win)

win.getMouse()
encode_box.undraw()
box_txt.undraw()

msg = msg_entry.getText().replace(" ", "").upper()
keywrd = keywrd_entry.getText().replace(" ", "").upper() * len(msg)

encoded_lst = []
# ord A = 65
# ord Z = 90
calc_var = 0
for i in range(len(msg)):
    calc_var += (ord(keywrd[i]) - 65) + (ord(msg[i]) - 65)
    calc_var = calc_var % 26
    encoded_lst.append(chr(calc_var + 65))
    calc_var = 0
output = "".join(encoded_lst)

result_pt = Point(win_width/2, 200)
result = Text(result_pt, "Resulting Message")
result.draw(win)

data_result_pt = Point(win_width/2, 225)
data_result = Text(data_result_pt, output)
data_result.draw(win)


close_msg_pt = Point(win_width/2, win_height - 25)
close_msg = Text(close_msg_pt, "Click Anywhere to Close Window")
close_msg.draw(win)
win.getMouse()
