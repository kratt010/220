class Button:
    def __init__(self, shape, label):
        from graphics import Text
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        p1 = self.shape.getP1()
        p2 = self.shape.getP2()
        if p1.getX() <= point.getX() <= p2.getX():
            if p1.getY() <= point.getY() <= p2.getY():
                return True
        elif p1.getX() >= point.getX() >= p2.getX():
            if p1.getY() >= point.getY() >= p2.getY():
                return True
        return False

    def color_button(self, color):
        self.shape.setFill(color)
