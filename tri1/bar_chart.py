# this is a turtle bar chart
import turtle


def drawBar(t, height):
    """Get turtle t to draw on bar, of height"""
    t.begin_fill()
    if height < 0:
        t.write(str(height))

    t.left(90)
    t.forward(height)
    if height >= 0:
        t.write(str(height))

    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


xs = [48, -50, 200, 240, 160, 260, 220]
maxheight = max(xs)
minheight = min(xs)
numbars = len(xs)
border = 10

turtle.color("blue")
turtle.fillcolor("red")
turtle.pensize(3)
wn = turtle.Screen()
wn.bgcolor("orange")
if minheight > 0:
    lly = 0
else:
    lly = minheight - border

wn.setworldcoordinates(0 - border, lly, 40 * numbars + border, maxheight+border)

for x in xs:
    drawBar(turtle, xs)

wn.exitonclick()
