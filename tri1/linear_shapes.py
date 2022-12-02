# --------------------
# Made by Brady Hodge
# Status: Graded
# --------------------

# import turtle and set up screen
import turtle
wn = turtle.Screen()

# ask user for the size of the square
size = float(input("What is the size of each square? "))

# create the for loop to draw the squares
for x in ["red", "green", "blue", "purple"]:
    turtle.color(x)
    for y in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.penup()
    turtle.forward(size+10)
    turtle.pendown()

wn.exitonclick()
