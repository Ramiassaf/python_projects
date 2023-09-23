from turtle import Turtle

STARTING_POSITION = (0, -280)   # Starting position for the player turtle
MOVE_DISTANCE = 10  # Distance to move the turtle each time it moves up
FINISH_LINE_Y = 280  # The finish line y-coordinate that the player needs to reach


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")  # Sets the shape of the turtle to the turtle icon
        self.color("red", "green")  # Sets the color of the turtle to black
        self.penup()  # Lifts the turtle pen so it doesn't draw lines
        self.setheading(90)  # Sets the turtle heading to 90 degrees (facing upwards)
        self.goto(STARTING_POSITION)  # Sets the turtle's starting position to the starting position

    def move_up(self):
        self.forward(MOVE_DISTANCE)  # Moves the turtle up by the move distance

    def finish(self):
        if self.ycor() == FINISH_LINE_Y:  # Checks if the turtle has reached the finish line
            # print("You reach the final line")  # Prints a message to indicate that the player has reached finish line
            self.goto(STARTING_POSITION)  # Sends the turtle back to the starting position
            return True  # Returns True to indicate that the player has finished the game
        else:
            return False  # Returns False to indicate that the player hasn't finished the game yet
