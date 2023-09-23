from turtle import Screen
from Paddle import Paddle
from ball import Ball
from Score import Score
import time
screen = Screen()
score = Score()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

# Turn off animation so that the screen updates only when we want it to
screen.tracer(0)
l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))
ball = Ball()
# Listen for keyboard events
screen.listen()

# When the keys pressed, to make the right and left paddle to move
screen.onkey(key="Up", fun=l_paddle.move_up)
screen.onkey(key="Down", fun=l_paddle.move_down)
screen.onkey(key="w", fun=r_paddle.move_up)
screen.onkey(key="s", fun=r_paddle.move_down)

game_is_on = True

# Start the game loop
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()  # call the move function from the ball class which increase the x and y coordinates

    # Detect collision with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:  # we chose 280 since the circle dimension is 20x20
        ball.bounce_y()

    # Detect Collision with the paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() > 320 or ball.distance(r_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Check if the ball didn't hit the paddle and refresh the game
    if ball.xcor() > 360:
        ball.refresh()
        score.l_point()

    if ball.xcor() < -360:
        ball.refresh()
        score.r_point()

    screen.update()
# Exit the program when the screen is clicked
screen.exitonclick()
