# Made by Brady Hodge
# CSE 110
# 04 Prove Assignment - Meal Price Calculator

"""
+ added "drink_price" and "numb_of_drinks" for stretch goal
+ added "tip_percent" and "tip_amount" for stretch goal
"""

# Ask the user for the price of a child and an adult meal and store these values properly into variables as floating point numbers.
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))

# Ask the user for the number of adults and children and store these values properly into variables as integers.
numb_of_children = int(input("How many children are there? "))
numb_of_adults = int(input("How many adults are there? "))

# Ask user how many and the price of drinks. (Stretch Goal)
drink_price = float(input("What is the price of a drink? "))
numb_of_drinks = int(input("How many drink orders are there? "))


# Ask the user for the sales tax rate and store the value properly as a floating point number.
sales_tax = float(input("What is the sales tax rate? "))

# Ask user how much tip they would like to leave. (Stretch Goal)
tip_percent = float(
    (input("What is the tip percentage? (enter a whole number) ")))

# Compute and display the subtotal.
subtotal = child_meal_price * numb_of_children + \
    adult_meal_price * numb_of_adults + drink_price * numb_of_drinks

print(f"\nSubtotal: ${subtotal:,.2f}")

# Compute and display the sales tax.
sales_tax_total = (sales_tax / 100) * subtotal
print(f"Sales tax: ${sales_tax_total:,.2f}")

# Display the tip. (Stretch Goal)
tip_amount = (tip_percent / 100) * subtotal
print(f"Tip: ${tip_amount:,.2f}")

# Compute and display the total.
total = subtotal + sales_tax_total + tip_amount
print(f"Total: ${total:,.2f}")

# Ask the user for the payment amount and store the value properly as a floating point number.
payment_amount = float(input("\nWhat is the payment amount? "))

# Compute and display the change.
change = payment_amount - total
print(f"Change: ${change:,.2f}")