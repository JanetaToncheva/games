from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

LEFT_POSITION = (-350, 0)
RIGHT_POSITION = (350, 0)
MOVE_DISTANCE = 20
UPPER_WALL_Y = 280
LOWER_WALL_Y = -280

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Game of Pong')
screen.tracer(0)

l_paddle = Paddle(LEFT_POSITION)
r_paddle = Paddle(RIGHT_POSITION)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
r_losses = 0
l_losses = 0

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with upper or lower wall
    if ball.ycor() > UPPER_WALL_Y or ball.ycor() < LOWER_WALL_Y:
        # needs to bounce down
        ball.y_bounce()

    # detect collision with r_paddle and l_paddle
    # distance between ball and paddle is measured at the respective centers
    # so if the ball hits the paddle off-center that also has to be covered
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.x_bounce()

    # detect if r_paddle misses and if yes, return ball to center and move towards other player
    if ball.xcor() > 390 and ball.distance(r_paddle) > 50:
        ball.reset_ball()
        scoreboard.l_point()
        # criteria to end the game after 15 missed balls on each side
        r_losses += 1

    # detect if l_paddle misses
    if ball.xcor() < -390 and ball.distance(l_paddle) > 50:
        ball.reset_ball()
        scoreboard.r_point()
        # criteria to end the game after 15 missed balls on each side
        l_losses += 1

    if r_losses > 3:
        game_is_on = False
        scoreboard.r_lose_game_over()
    elif l_losses > 3:
        game_is_on = False
        scoreboard.l_lose_game_over()


screen.exitonclick()
