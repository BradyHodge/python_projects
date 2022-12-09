# Made by Brady Hodge
# CSE 110
# 05 Prepare: Checkpoint - Practicing If Statements

first_numb = int(input("What is the first number? "))
second_numb = int(input("What is the second number? "))

if first_numb > second_numb:
    print("The first number is greater")
else:
    print("The first number is not greater")

if first_numb == second_numb:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if second_numb > first_numb:
    print("The second number is greater")
else:
    print("The second number is not greater")

print() # Blank line

user_animal = input("What is your favorite animal? ")

if user_animal.lower() == "bear":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")