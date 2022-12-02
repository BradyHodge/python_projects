# Made by Brady Hodge
# CSE 110
# 03 Prove: Milestone - Meal Price Calculator

"""
+ added "drink_price" for stretch goal
+ added "tip_percent" for stretch goal
"""

# part 1

# ask user for the price and the Number of meals
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
numb_of_children = int(input("How many children are there? "))
numb_of_adults = int(input("How many adults are there? "))

drink_price = float(input("What is the price of a drink? "))
numb_of_drinks = int(input("How many drink orders are there? "))
# sales tax
sales_tax = float(input("What is the sales tax rate? "))

# calculate subtotal
subtotal = child_meal_price * numb_of_children + \
    adult_meal_price * numb_of_adults + drink_price * numb_of_drinks

print(f"Subtotal: ${subtotal:,.2f}")

tip_percent = float((input("What is the tip percentage? (enter a whole number) ")))

# calculate tip
tip_amount = (tip_percent / 100) * subtotal