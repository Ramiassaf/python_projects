from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")   # sets the color of the turtle to black
        self.penup()          # lifts the turtle's pen off the screen
        self.level = 1        # initializes the level to 1
        self.hideturtle()     # hides the turtle
        self.score_layout()   # calls the score_layout method

    def score_layout(self):
        self.clear()     # clears the turtle's previous writing on the screen
        self.goto(-275, 260)     # sets the position where the turtle should write the score
        self.write(f"Level:{self.level}", align="left", font=FONT)  # writes the score on the screen
        # with the specified font and alignment

    def update_score(self):
        self.level += 1    # increases the level by 1
        self.score_layout()  # calls the score_layout method to update the score

    def game_over(self):
        self.goto(0, 0)   # sets the position where the turtle should write "GAME OVER"
        self.write("GAME OVER", align="center", font=FONT)  # writes "GAME OVER" on the screen
        # with the specified font and alignment
