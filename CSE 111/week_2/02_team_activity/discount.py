# Made by Brady Hodge
# CSE 111
# 02 Team Activity: Calling Functions

from datetime import datetime

current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
day_of_week = 2

subtotal = float(input("Please enter the subtotal: "))


if day_of_week == 1 or day_of_week == 2:
    discount = 0.1
else:
    discount = 0

discount_subtotal_amount = round(subtotal * discount, 2)
sales_tax_amount = ((subtotal - discount_subtotal_amount) * 0.06) # used the wrong var
total = (subtotal + sales_tax_amount)

if discount != 0:
    print(f"Discount amount: {discount_subtotal_amount}")
print(f"Sales tax: {sales_tax_amount:.2f}")
print(f"Total: {total:.2f}")


