from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.7)
        self.goto(0, -100)
        self.setheading(45)

    def move(self):
        self.forward(10)

    def bounce_y(self):
        current_heading = self.heading()
        self.setheading(360 - current_heading)

    def bounce_x(self):
        current_heading = self.heading()
        self.setheading(180 - current_heading)

    def reset_position(self):
        self.goto(0, -100)
        self.setheading(45)
