from turtle import Turtle
import random


class Food(Turtle):  # by this I create a new class and I inherent all the methods found in turtle package in it
    def __init__(self):
        super().__init__()  # self here iit means the Turtle
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # making the circle dimension 10 by 10 originally the
        # turtle size is 20 20
        self.color('blue')
        self.speed("fastest")

    def refresh(self):  # this method is giving the new turtle which have circle shape and
        # basically it's the food a new cord
        xcor = random.randint(-288, 289)
        ycor = random.randint(-289, 289)
        self.goto(xcor, ycor)
