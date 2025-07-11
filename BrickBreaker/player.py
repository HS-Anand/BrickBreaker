from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=0.4, stretch_len=3)
        self.goto(0,-200)

    def left(self):
        if self.heading() == RIGHT:
            self.setheading(LEFT)

    def right(self):
        if self.heading() == LEFT:
            self.setheading(RIGHT)

    def move(self):
            x = self.xcor()
            if x > -320 and self.heading() == LEFT:
                self.forward(10)
            elif x < 310 and self.heading() == RIGHT:
                self.forward(10)


