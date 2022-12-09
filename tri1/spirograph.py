# --------------------
# Made by Brady Hodge
# Status: Graded
# --------------------

import turtle
wn = turtle.Screen()
jeff = turtle.Turtle()
jeff.speed(0)

for graph in range(30):
    jeff.right(12)
    for square in range(4):
        jeff.forward(200)
        jeff.right(90)

wn.exitonclick()
