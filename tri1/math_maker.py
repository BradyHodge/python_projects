# --------------------
# Made by Brady Hodge
# Status: done
# --------------------

# Ask the user for a whole first number
first_number = int(input("What is the first number? "))

# Ask the user for a whole second number
second_number = int(input("What is the second number? "))

# Sum the numbers
number_sum = first_number + second_number

# Get the product
number_product = first_number * second_number

# Get the difference
number_difference = first_number - second_number

# The quotient of the first number divided by the second using floating point division
number_quotient_floating = first_number / second_number

# The quotient of the first number divided by the second using integer division
number_quotient_integer = first_number // second_number

# Get the modulus of the first number using the second.
number_modulus = first_number % second_number

# Raise the first number to the power of the second.
number_power = first_number ** second_number

# rounding
for number in [number_power, number_modulus, number_quotient_integer, number_quotient_floating,
               number_difference, number_product, number_sum]:
    number = format(number, ".3f")

# print number
print("---------------------------")
print("sum        :", round(number_sum, 3))
print("Product    :", round(number_product, 3))
print("Difference :", round(number_difference, 3))
print("F-Quotient :", round(number_quotient_floating, 3))
print("I-Quotient :", round(number_quotient_integer, 3))
print("Modulus    :", round(number_modulus, 3))
print("Exponential:", round(number_power, 3))
