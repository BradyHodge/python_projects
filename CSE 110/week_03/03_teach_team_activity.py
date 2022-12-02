# Made by Brady Hodge
# CSE 110
# 03 Teach: Team Activity - Areas of Shapes

import math

# area of a square
length_square = float(input("What is the length of a side of the square? "))

area_square = length_square * length_square
print(f"The area of the square is: {area_square}")

# area of a rectangle
length_rectangle = float(input("What is the length of a side of the rectangle? "))
width_rectangle = float(input("What is the width of a side of the rectangle? "))

area_rectangle = length_rectangle * width_rectangle
print(f"The area of the rectangle is: {area_rectangle}")

# area of a circle
radius_circle = float(input("What is the radius of the circle? "))

area_circle = math.pi * (radius_circle * radius_circle)
print(f"The area of the circle is: {area_circle}")

# single input value 
value = float(input("What is the value to be used? "))

area_square = value ** 2
area_circle = math.pi * (value ** 2)
volume_cube = value ** 3
volume_sphere = (4 / 3) * math.pi * (value ** 3)

print(f"Area of a square: {area_square}")
print(f"Area of a circle: {area_circle}")
print(f"Volume of a cube: {volume_cube}")
print(f"Volume of a sphere: {volume_sphere}")