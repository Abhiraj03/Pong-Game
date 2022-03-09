from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True

time_speed = 0.1

while game_is_on:
    screen.update()
    time.sleep(time_speed)
    scoreboard.update_scoreboard()
    ball.move()
    if ball.ycor() >= 290  or ball.ycor() <= -290:
        ball.bounce()
    
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320:
        ball.hit()
        scoreboard.r_board()
        time_speed -= 0.01
    
    if ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.hit()
        scoreboard.l_board()
        time_speed -= 0.01
    
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.reset()
        time_speed = 0.1


















screen.exitonclick()


