from turtle import Turtle

LEFT_POSITION = (350, 0)
RIGHT_POSITION = (-350, 0)
WIDTH_COEFF = 5
MOVE_DISTANCE = 20
# UP = 90
# DOWN = 270


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape('square')
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=WIDTH_COEFF, stretch_len=1)
        self.color('white')

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
