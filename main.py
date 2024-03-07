from turtle import *
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

s = Screen()                 # screen object
s.setup(width=600, height=600)              # display size
s.bgcolor("black")              # screen bg color
s.title("Snake Game")            # title of screen
s.tracer(0)                     # move togather

snake = Snake()                 # 1. snake class obj
food = Food()                   # 2. food class obj
scoreboard = ScoreBoard()       # 3. Score_Board class obj

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")
# snake body
# segments = []


# movement
game_is_on = True
while game_is_on:
    s.update()                  # continues motion
    time.sleep(0.15)
    snake.move()                # function call
    # for seg in segments:
    #     seg.forward(20)
    #
    # segments[0].left(90)
# control range
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

s.exitonclick()                 # hold screen
