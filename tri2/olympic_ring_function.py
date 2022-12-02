# ----------------------
# Made by Brady Hodge
# Status: Graded
# Date Started: 30/3/22
# ----------------------

# Draws the Olympic rings using Turtle Graphics and uses a function

# import turtle
from turtle import *


# create a function that draws a ring at a specified location, color, and radius.
def draw_ring(xcoord, ycoord, ring_color, ring_radius, turtle):
    turtle.up()
    turtle.goto(xcoord, ycoord)
    turtle.down()
    turtle.color(ring_color)
    turtle.circle(ring_radius)


# setup
setup(width=500, height=500, startx=0, starty=50)
deez = Turtle()
deez.width(3)
ring_radius = 75
title("olympic_rings.py program using a function")

# draw the 5 rings by making call to the draw_ring Function.
draw_ring(-100, 0, "blue", ring_radius, deez)
draw_ring(0, 0, "black", ring_radius, deez)
draw_ring(100, 0, "red", ring_radius, deez)
draw_ring(-50, -75, "yellow", ring_radius, deez)
draw_ring(50, -75, "green", ring_radius, deez)

# cleanup and exit
deez.hideturtle()
done()
