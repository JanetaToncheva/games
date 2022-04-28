import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create and move the cars
    car_manager.generate_car()
    car_manager.move()

    # detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # detect player levelling up
    if player.ycor() == FINISH_LINE_Y:
        player.reset_turtle()
        scoreboard.level_up()
        car_manager.move_faster()

screen.exitonclick()
