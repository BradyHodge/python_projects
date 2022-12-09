# --------------------
# Made by Brady Hodge
# Status: Graded
# --------------------

# import turtle
import turtle
win = turtle.Screen()
jeff = turtle.Turtle()

jeff.penup()
jeff.forward(-300)
jeff.pendown()

# draw equilateral triangle
for t in range(3):
    jeff.forward(50)
    jeff.left(120)

jeff.penup()
jeff.forward(150)
jeff.pendown()

# draw square
for s in range(4):
    jeff.forward(50)
    jeff.left(90)

jeff.penup()
jeff.forward(150)
jeff.pendown()

# draw hexagon
for h in range(6):
    jeff.forward(50)
    jeff.left(60)

jeff.penup()
jeff.forward(150)
jeff.pendown()

# draw octagon
for o in range(8):
    jeff.forward(50)
    jeff.left(45)

win.exitonclick()
