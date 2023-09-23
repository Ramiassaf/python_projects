# Import the Turtle class from the turtle module
from turtle import Turtle


# Define a new class called Paddle that inherits from the Turtle class
class Paddle(Turtle):

    # Define the __init__ method, which is called when a new instance of the Paddle class is created
    def __init__(self, position):
        # Call the __init__ method of the Turtle class to initialize the Turtle object
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        # Set the initial position of the Paddle
        self.goto(position)

    # Define the move_up method, which moves the Paddle up by 20 pixels
    def move_up(self):
        new_y = self.ycor() + 20
        if new_y < 250:
            self.goto(self.xcor(), new_y)

    # Define the move_down method, which moves the Paddle down by 20 pixels
    def move_down(self):
        new_y = self.ycor() - 20
        if new_y > -250:
            self.goto(self.xcor(), new_y)
