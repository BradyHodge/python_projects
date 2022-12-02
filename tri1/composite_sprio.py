# --------------------
# Made by Brady Hodge
# Status: Done
# --------------------
import turtle

wn = turtle.Screen()
turtle.speed(0)


# create a function to draw a square
def square():
    for x in range(4):
        turtle.forward(200)
        turtle.right(90)


# create a function to use the square function and rotate the square
def sprio():
    for y in range(30):
        turtle.right(12)
        square()


sprio()

wn.exitonclick()
