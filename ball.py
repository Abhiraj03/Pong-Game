from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.goto(20,20)
    
    def move(self):
        self.inc = 10
        self.goto(self.xcor() + self.inc, self.ycor() + self.inc)

    def turn(self):
        self.setheading(self.heading() + 180)