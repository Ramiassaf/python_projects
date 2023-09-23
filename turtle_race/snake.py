from turtle import Turtle
import random
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # creating a tuple list of the starting position of the three turtles
#  IT'S CAPITALIZED SINCE IN PYTHON WE ALWAYS WRITE THE CONSTANT IN A CAPITALIZED CASE
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
COLORS = ["Dodger Blue", "Indian Red", "Light Salmon", "Light Sea Green", "Light Slate Gray"]


class Snake:

    def __init__(self):
        self.segments = []  # I'm adding the three squares created in the for loop in it
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("Light Gray")

    def create_snake(self):  # here we are creating our snake
        for position in STARTING_POSITION:  # here basically will loop 3 times creating the turtles(square shape)
            # and each turtle will start in an initial position
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color(random.choice(COLORS))
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("Light Gray")

    def extend(self):
        self.add_segment(self.segments[-1].position())  # I'm holding the position of the last turtle
        # which is last square
        # then call the add segment function that will add the segments list a new square

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # watch day 20 video 185 Animating
            # the Snake segments on screen
            new_x = self.segments[seg_num - 1].xcor()  # here to make the snake move with each
            # other since it consists of 3 different squares
            new_y = self.segments[seg_num - 1].ycor()  # here I'm telling that square
            # number 3 to get the coordinate of square number 2
            self.segments[seg_num].goto(new_x, new_y)  # here I'm telling square
            # number 3 to go to the place of square number 2 and also when the loop moves 2 will go to 1
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
