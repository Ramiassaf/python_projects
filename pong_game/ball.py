from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # A move method to move the ball
    def move(self):
        # Calculate new coordinates for the ball
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        # Set the ball's position to the new coordinates
        self.goto(new_x, new_y)

    # we're only multiplying the y coordinates by -1 so instead of increasing it will decrease
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9  # making the ball move faster each time it hits the paddle
        # by incrementing the delay of the program execution

    # This method refreshes the ball's position and changes its direction
    def refresh(self):
        # Move the ball back to the center of the screen
        self.goto(0, 0)
        self.move_speed = 0.1  # when we refresh the game we return the time to its beginning
        self.bounce_x()


