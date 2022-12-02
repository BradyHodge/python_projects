# Draw 5 squares, 20 units per side. Use a functon

import turtle


def drawsquare(t, sz):
    """Make turtle t draw a square of with side sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("hotpink")
alex.pensize(3)

size = 20
for i in range(5):
    drawsquare(alex, size)
    alex.penup()
    alex.forward(-10)
    alex.right(90)
    alex.forward(10)
    alex.left(90)
    alex.pendown()
    size = size + 20

wn.exitonclick()
