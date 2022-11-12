# Draw a polygon

def drawPoly(someturtle, somesides, somesize):
    for poly in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(360 / somesides)


import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)

drawPoly(tess, 8, 50)

wn.exitonclick()
