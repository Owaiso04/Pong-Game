import turtle
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position: tuple):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_len=5)
        self.setheading(90)
        self.penup()
        self.goto(position)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
