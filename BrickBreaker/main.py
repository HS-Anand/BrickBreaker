from turtle import Screen
from player import Player
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(700, 500)
screen.bgcolor("black")
screen.title("Brick Breaker")
screen.tracer(0)

# Objects
player = Player()
ball = Ball()
bricks = Brick()
scoreboard = Scoreboard()

# Key bindings
screen.listen()
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.03)

    player.move()
    ball.move()

    # Paddle collision
    if ball.ycor() < -210 and player.xcor() - 50 < ball.xcor() < player.xcor() + 50:
        ball.bounce_y()

    # Wall collision
    if ball.xcor() >= 340 or ball.xcor() <= -340:
        ball.bounce_x()

    if ball.ycor() >= 240:
        ball.bounce_y()

    # Brick collision
    for brick in bricks.segment[:]:
        if ball.distance(brick) < 30:
            brick.hideturtle()
            bricks.segment.remove(brick)
            ball.bounce_y()
            scoreboard.increase_score()

    # Ball falls below paddle
    if ball.ycor() <= -250:
        ball.reset_position()


    # Win condition
    if len(bricks.segment) == 0:
        scoreboard.win()
        game_on = False

screen.exitonclick()
