import time  # import the time module for pausing the game
from turtle import Screen  # import the Screen class from turtle module
from player import Player  # import the Player class from player module
from car_manager import CarManager  # import the CarManager class from car_manager module
from scoreboard import Scoreboard  # import the Scoreboard class from scoreboard module

# create a Screen object
screen = Screen()
screen.setup(width=600, height=600)  # set the dimensions of the screen
screen.title("Turbo Turtle")  # set the title of the screen
screen.tracer(0)  # turn off the screen animation

# create Player, Scoreboard, and CarManager objects
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True  # set a boolean variable to indicate if the game is running
screen.listen()  # listen for keyboard events
screen.onkey(key="Up", fun=player.move_up)  # call move_up method when up arrow key is pressed

while game_is_on:
    time.sleep(0.1)  # pause the game for 0.1 seconds
    screen.update()  # update the screen
    car_manager.create_car()  # create a new car
    car_manager.move_cars()  # move all the cars in the car list
    for car in car_manager.all_cars:  # iterate through all the cars
        if player.distance(car) < 23:  # check if the player collides with a car
            scoreboard.game_over()  # display game over message
            game_is_on = False  # set False to stop the game
            screen.exitonclick()  # exit the game when clicked

    if player.finish():  # check if the player reaches the finish line
        car_manager.speed_up()  # speed up all the cars in the car list
        scoreboard.update_score()  # update the score on the scoreboard
