# ----------------------
# Made by Brady Hodge
# Status: Graded
# lab 16.2; 1/1
# ----------------------
import turtle
import random


def tree(branchLen, t):
    if branchLen > 5:
        t.color("brown")
        t.pensize(branchLen / 15)
        t.forward(branchLen)
        t.right(20)
        tree(random.randrange(branchLen - 25, branchLen - 5), t)
        t.left(40)
        tree(random.randrange(branchLen - 25, branchLen - 5), t)
        t.right(20)
        t.backward(branchLen)
        t.color("brown")
    elif 5 >= branchLen > 0:
        t.color("green")
        t.pensize(branchLen / 15)
        t.forward(branchLen)
        t.right(20)
        tree(random.randrange(branchLen - 25, branchLen - 5), t)
        t.left(40)
        tree(random.randrange(branchLen - 25, branchLen - 5), t)
        t.right(20)
        t.backward(branchLen)
        t.color("brown")


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.speed(0)
    tree(100, t)
    myWin.exitonclick()


main()