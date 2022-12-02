# --------------------
# Made by Brady Hodge
# Status: Graded
# --------------------

import turtle
win = turtle.Screen()
turt = turtle.Turtle()
turt.speed(0)

# user input
number_sides = int(input("How many sides does the polygon have? "))
length_sides = float(input("What is the length of the sides? "))
color_sides = str(input("What is the color of the polygon? "))

# angle calculations
angle = 360 / number_sides

# set color
turt.fillcolor(color_sides)
turt.begin_fill()

# move turtle
for move in range(number_sides):
    turt.forward(length_sides)
    turt.left(angle)

# end fill
turt.end_fill()

win.exitonclick()
