
from turtle import Turtle
import random


class Food(Turtle):
    COLORS = ["red", "blue", "green", "yellow", "orange", "purple"]

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(self.COLORS))
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
