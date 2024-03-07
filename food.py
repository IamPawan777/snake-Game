from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()          # get turtle module fun's
        self.shape("circle")        # shape of food
        self.penup()                # up the pen form screen
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')               # color of food
        self.speed("fastest")  # food appear fastly
        self.refresh()
    def refresh(self):
        random_x = randint(-280, 280)  # random appear food in x direction
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)

