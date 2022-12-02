# --------------------
# Made by Brady Hodge
# Status: Done
# --------------------



import turtle
win = turtle.Screen() # made screen
bob = turtle.Turtle() # named turtle
bob.color("black")

king_george = turtle.Turtle()
paul = turtle.Turtle()
jess = turtle.Turtle()

king_george.color("red")
paul.color("green")
jess.color("blue")

for i in range(22):
    jess.left(20)
    jess.forward(20)
jess.left(90)
jess.forward(60)
jess.left(120)
jess.forward(70)

for i in range(22):
    paul.left(20)
    paul.forward(20)
paul.left(90)
paul.forward(60)
paul.left(120)
paul.forward(70)

for i in range(22):
    king_george.left(20)
    king_george.forward(20)
king_george.left(90)
king_george.forward(60)
king_george.left(120)
king_george.forward(70)

king_george.forward(300)
paul.right(300)
paul.forward(300)
jess.left(300)
jess.forward(300)

for i in range(22):
    bob.left(20)
    bob.forward(20)
bob.left(90)
bob.forward(60)
bob.left(120)
bob.forward(70)



win.exitonclick()
