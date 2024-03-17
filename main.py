import turtle
import time

screen = turtle.Screen()
t = turtle.Turtle()

t.penup()
t.goto(0, -150)
t.pendown()
t.color('red')
t.begin_fill()
t.circle(150)
t.end_fill()
t.penup()
t.goto(0, -100)
t.pendown()
t.begin_fill()
t.color("white")
t.circle(100)
t.end_fill()
t.right(45)
t.penup()
t.goto(0, 0)
t.pendown()
t.color("black")
t.width(10)

for i in range(4):
    t.forward(65)
    t.right(90)
    t.forward(65)
    t.penup()
    t.goto(0, 0)
    t.pendown()

turtle.done()