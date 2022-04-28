from turtle import Turtle

FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 1
        self.color('black')
        self.write_score()

    def write_score(self):
        self.goto(-280, 250)
        self.write(f"Level {self.score}", align='left', font=FONT)

    def level_up(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align='center', font=FONT)


