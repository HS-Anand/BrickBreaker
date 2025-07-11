import random
from turtle import Turtle

color = ("red","green","yellow","orange","purple","cyan")


class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.make()

    def make(self):
        self.x = 320
        self.y = 20
        self.segment = []
        for y in range(8):
            self.x = 320
            self.y = self.y + 30
            for x in range(14):
                r = random.randint(0, 1)
                if (r == 1):
                    self.create()
                elif (r == 0):
                    self.x = self.x - 50

    def create(self):
        new = Turtle()
        new.shape("square")
        new.penup()
        new.shapesize(stretch_wid=0.7, stretch_len=2)
        new.color(random.choice(color))
        new.goto(self.x,self.y)
        self.x=self.x-50
        self.segment.append(new)
