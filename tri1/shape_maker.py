# --------------------
# Made by Brady Hodge
# Status: Graded
# --------------------

# import turtle
import turtle

# define window and speed
wn = turtle.Screen()
turtle.speed(0)

# define number of shapes (input from user)
shape_num = int(input("How many shapes should I draw? "))

# FOR loop that repeats for every shape
for x in range(shape_num):
    # print current shape number
    print("For shape ", x + 1, ": ", sep="")
    # define number of lines for current shape (input from user)
    lines = int(input("      How many lines should I draw? "))
    # define angles for current shape (input from user)
    angle = float(input("      What angle should I turn each time? "))
    # draw current shape
    for y in range(lines):
        turtle.forward(35)
        turtle.left(angle)
    # repeat for all shapes

wn.exitonclick()
