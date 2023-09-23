from turtle import Turtle  # Import the Turtle class from the turtle module

ALIGNMENT = "center"  # Define a constant variable for text alignment
FONT = ("Arial", 24, "normal")  # Define a constant variable for font style


class Score(Turtle):  # Define a Score class that inherits from the Turtle class

    def __init__(self):  # Define the constructor for the Score class
        super().__init__()  # Call the constructor of the parent class
        self.color('White')  # Set the turtle's color to white
        self.score = 0  # Initialize the score to zero by default

        # Open and read the contents of a data to retrieve the high score
        with open("data.txt", mode="r") as data:
            content = data.read()
            if content:
                self.high_score = int(content)

        self.penup()  # Don't draw while moving the turtle
        self.hideturtle()  # Hide the turtle
        self.goto(0, 260)  # Move the turtle to the top center of the screen
        self.update_score()  # Call the update_score method to display the score on the screen

    def update_score(self):  # Define a method to update the score
        self.clear()  # Clear the previous score display
        # Display the current and highest score on the screen with a specified alignment and font style
        self.write(f"Score: {self.score} Highest Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def score_reset(self):  # Define a method to reset the score
        # Check if the current score is greater than the high score and update it accordingly
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))  # Write the new high score to the file
        self.score = 0  # Reset the score to zero
        self.update_score()  # Call the update_score method to display the new score on the screen

    def increase_score(self):  # Define a method to increase the score
        self.score += 1  # Increase the score by 1
        self.update_score()  # Call the update_score method to display the new score on the screen
