import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import car_manager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
PLAYER = Player()
scoreboard = Scoreboard()
screen.listen()
car_manager = car_manager()

game_is_on = True

while game_is_on:
    screen.onkey(PLAYER.move, "Up")
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move()
    if PLAYER.check_crossed():
        scoreboard.level_update()
        car_manager.speed_up()
    for car in car_manager.all_cars:
        if car.distance(PLAYER) < 20:
            scoreboard.game_over()
            game_is_on = False
screen.exitonclick()
