# --------------------
# Made by Brady Hodge
# Status: done
# --------------------

# create turtle and screen
import turtle
happy = turtle.Turtle()
win = turtle.Screen()


# set color
col = "purple"

# set the fillcolor
happy.fillcolor(col)

# start the fillcolor
happy.begin_fill()

# draw a square
for x in range(4):
    happy.forward(280)
    happy.right(90)

# exit filling color
happy.end_fill()

win.exitonclick()
