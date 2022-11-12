# ----------------------
# Made by Brady Hodge
# Status: Graded
# lab 16.3; 1/1
# ----------------------
import turtle
import random


def triangle(go):
    t.forward(go)
    t.left(120)
    t.forward(go)
    t.left(120)
    t.forward(go)

    t.left(120)
    t.forward(random.randrange(int(-go/2), int(go/2)))
    next_go = (go / 2) + (go / 4)
    triangle(next_go)


t = turtle.Turtle()
myWin = turtle.Screen()
turtle.Screen().bgcolor('black')
t.color('white')

t.penup()
t.goto(0, -350)
t.pendown()
triangle(800)

turtle.done()
