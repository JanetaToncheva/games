from turtle import Turtle

FONT = ('Courier', 20, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        with open('data.txt') as data:
            high_score = data.read()
        self.highest_score = int(high_score)
        self.color('white')
        self.goto(0, 270)
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}. Highest score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def reset_board(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        with open('data.txt', mode='w') as data:
            data.write(f"{self.highest_score}")
        self.score = 0
        self.write_score()

    # def write_game_over(self):
    #     self.goto(0, 0)
    #     self.write('Game Over', align=ALIGNMENT, font=FONT)