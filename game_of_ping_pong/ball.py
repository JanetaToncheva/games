from turtle import Turtle

UPPER_WALL_Y = 280
LOWER_WALL_Y = -280


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.06 #this will be used in time.sleep as speed so the lower the number, faster the speed

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self): # this is when it hits the paddle
        self.x_move *= -1
        self.move_speed *= 0.9 #reduces the sleep time hence makes the

    def reset_ball(self):
        self.goto(0, 0)
        self.x_bounce()
        self.move_speed = 0.1




