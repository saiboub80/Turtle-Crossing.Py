<<<<<<< HEAD
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
=======
from turtle import Screen
from cars import Cars
from player import Player
import time
from score import Score
>>>>>>> e5cfd15 (Initial commit)

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

<<<<<<< HEAD
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
=======
player = Player()
cars = Cars()
score = Score()

screen.listen()
screen.onkey(player.go_up,'Up')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move_cars()

    #Detect collision with car
    for car in cars.all_CARS:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        cars.level_up()
        score.increase_level()


screen.exitonclick()
>>>>>>> e5cfd15 (Initial commit)
