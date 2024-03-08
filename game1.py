from turtle import  Screen
from sanke import Snake
from score import Score
from food import Food
import time
src = Screen()
src.bgcolor("black")
src.setup(width=600, height=600)
src.tracer(0)
snake = Snake()
food = Food()
scorebord = Score()
src.listen()
src.onkey(snake.up, "Up")
src.onkey(snake.down, "Down")
src.onkey(snake.right, "Right")
src.onkey(snake.left, "Left")
gameon = True
while gameon:
    src.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scorebord.incress_score()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        gameon = False
        scorebord.game_over()
    for seq in snake.segments:
        if seq == snake.head:
            pass
        elif snake.head.distance(seq) < 10:
            scorebord.game_over()


src.exitonclick()


