# Made by Brady Hodge
# CSE 110
# 13 Teach: Team Activity - Areas of Shapes Revisited

# import 
import math

# functions 

def compute_area_square(side):
    area = compute_area_rectangle(side, side)
    return area

def compute_area_rectangle(length, width):
    area = length * width
    return area

def compute_area_circle(radius):
    area = math.pi * radius * radius
    return area

def compute_area_triangle(base, height):
    area = 0.5 * base * height
    return area

def compute_area(shape, value1, value2=0):
    area = -1

    if shape == "square":
        area = compute_area_square(value1)
    elif shape == "circle":
        area = compute_area_circle(value1)
    elif shape == "rectangle":
        area = compute_area_rectangle(value1, value2)
    
    return area


# define varables
keep_going = True


while keep_going:
    # get user input
    shape = input("What shape would you like to calculate the area of? (square, rectangle, circle) ").lower()
    if shape == "square":
        side = float(input("What is the length of the side? "))
        area = compute_area(shape, side)
        print(f"The area is {area}")
    elif shape == "rectangle":
        length = float(input("What is the length? "))
        width = float(input("What is the width? "))
        area = compute_area(shape, length, width)
        print(f"The area is {area}")
    elif shape == "circle":
        radius = float(input("What is the radius? "))
        area = compute_area(shape, radius)
        print(f"The area is {area}")
    else:
        print("That is not a valid shape.")
    
    # ask if they want to go again
    go_again = input("Would you like to calculate another area? (yes or no) ").lower()
    if go_again == "no":
        keep_going = False