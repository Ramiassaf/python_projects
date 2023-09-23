from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()  # this will make the screen to listen to what you type on Keyboard
screen.onkey(key="Up", fun=snake.up)  # these are called High order function because they are using function as an
# argument
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # determine Collision with food
    if snake.head.distance(food) < 15:  # when the distance between the snake and the food less than 15 call the
        # refresh method
        food.refresh()
        snake.extend()
        score.increase_score()  # when the head of the snake hits the food the score will increase by 1

    # Detect Collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score.score_reset()
        snake.reset()

    # Detect Collision with tail
    for segment in snake.segments[1:]:  # we need to loop with all the segment that form the body of the
        # snake and here we
        # are using slicing to remove the head from the segments list im taking from index 1 up to the end
        if snake.head.distance(segment) < 10:
            score.score_reset()
            snake.reset()

screen.exitonclick()
