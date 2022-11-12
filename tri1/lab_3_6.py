# --------------------
# Made by Brady Hodge
# Status: Done
# --------------------

# import resources
import turtle
wn = turtle.Screen()
turtle = turtle.Turtle()

# user input
legs = int(input("How many legs does the sprite have? "))


# calculations for angles
angle = 360 / legs
angle = int(angle)

# draw legs
turtle.speed(0)
for x in range(legs):
    for y in range(angle):
        turtle.forward(1)
        turtle.left(1)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)
    turtle.right(90)

# smiley face
turtle.penup()
turtle.left(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(20)

turtle.pendown()
for a in range(360):
    turtle.right(1)
    turtle.forward(0.1)
turtle.penup()

turtle.forward(20)

turtle.pendown()
for b in range(360):
    turtle.right(1)
    turtle.forward(0.1)
turtle.penup()


turtle.forward(-20)
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.pendown()
turtle.left(-70)

for c in range(150):
    turtle.left(1)
    turtle.forward(0.2)

turtle.penup()
turtle. forward(500)

wn.exitonclick()
