# --------------------
# Made by Brady Hodge
# Status: Graded
# --------------------

import turtle

wn = turtle.Screen()
jeff = turtle.Turtle()

wn.bgcolor("black")
jeff.speed(0)
jeff.penup()

jeff.color("red")
for x in range(0, 60):
    jeff.left(x)
    jeff.forward(x)
    jeff.stamp()

jeff.color("orange")
for x in range(60, 120):
    jeff.left(x)
    jeff.forward(x)
    jeff.stamp()

jeff.color("yellow")
for x in range(120, 180):
    jeff.left(x)
    jeff.forward(x)
    jeff.stamp()

jeff.color("green")
for x in range(180, 240):
    jeff.left(x)
    jeff.forward(x)
    jeff.stamp()

jeff.color("blue")
for x in range(240, 300):
    jeff.left(x)
    jeff.forward(x)
    jeff.stamp()

jeff.color("purple")
for x in range(300, 360):
    jeff.left(x)
    jeff.forward(x)
    jeff.stamp()

wn.exitonclick()
