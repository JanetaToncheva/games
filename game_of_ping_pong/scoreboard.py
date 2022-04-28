from turtle import Turtle

FONT = ('Verdana', 40, 'normal')
ALIGNMENT = 'center'

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.write_score()

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.write_score()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.goto(120, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
        self.goto(-120, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)

    def l_lose_game_over(self):
        self.goto(-160, 150)
        self.write('Too many misses\nYou lose', align=ALIGNMENT, font=('Verdana', 16, 'normal'))

    def r_lose_game_over(self):
        self.goto(160, 150)
        self.write('Too many misses\nYou lose', align=ALIGNMENT, font=('Verdana', 16, 'normal'))

