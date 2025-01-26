import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG!")
screen.tracer(0)

paddle_1 = Paddle((380, 0))
paddle_2 = Paddle((-380, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(paddle_1) < 50 and ball.xcor() > 350) or (
        ball.distance(paddle_2) < 50 and ball.xcor() < -350
    ):
        ball.bounce_x()

    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
