# --------------------
# Made by Brady Hodge
# Status: Graded
# --------------------

import turtle


def shape(x):
    """Draws a shape based on angle x"""
    for y in range(1, 100):
        turtle.right(x)
        turtle.forward(y*2)
    turtle.right(x)


# turtle set up
wn = turtle.Screen()
wn.bgcolor("light green")
turtle.color("blue")
turtle.speed(0)

# Moving turtle to starting point for shape 1
turtle.penup()
turtle.forward(-200)
turtle.pendown()

# Draw shape 1
shape(90)

# Moving turtle to starting point for shape 2
turtle.penup()
turtle.forward(400)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.pendown()

# Draw shape 2
shape(89)

wn.exitonclick()
