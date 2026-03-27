from  turtle import Turtle,Screen
from snake import Snack
from food import Food
from scoreBoard import ScoreBoard


import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snack Game ")
screen.tracer(0)

snake = Snack()
food = Food()
scoreBoard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game_is_on = True
while game_is_on :
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend()
        scoreBoard.score_increase()
    if snake.head.xcor() > 280 or snake.head.xcor()< -280 or  snake.head.ycor() > 280 or snake.head.ycor()< -280:
        game_is_on = False
        scoreBoard.game_over()
    for segement in snake.segment[1:]:

        if snake.head.distance(segement) < 10 :
            game_is_on = False
            scoreBoard.game_over()

screen.exitonclick()


