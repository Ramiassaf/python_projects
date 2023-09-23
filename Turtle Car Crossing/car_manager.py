# import necessary modules
from turtle import Turtle
import random

# set up constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# create CarManager class
class CarManager:
    def __init__(self):
        # initialize instance variables
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE  # initializing default value

    # create a new car
    def create_car(self):
        # randomly choose whether to create a car or not
         random_chance = random.randint(1, 7)  # line random_chance = random.randint(1, 6) is used to create
        # a probability of 1 in 6 (or approximately 17%) of a new car being created in each frame of the game.
         if random_chance == 1:
            # create a new car with a random color and position
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)  # Since only we need it to change its y coordinates when starting
            new_car.goto(300, random_y)
            # add the new car to the list of all cars
            self.all_cars.append(new_car)

    # move all cars backwards
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)  # backward to make it move from right to left

    # increase car speed
    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
