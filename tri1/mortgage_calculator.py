# --------------------
# Made by Brady Hodge
# Status: Graded
# --------------------

# user input
home_price_str = input("What is the total amount of the home? $")
interest_rate_str = input("What is the interest rate? %")
loan_length_str = input("What is the length of the loan in months? ")

# Change to float
home_price_float = float(home_price_str)
interest_rate_float = float(interest_rate_str)
loan_length_float = float(loan_length_str)

# calculations
interest_rate_float = interest_rate_float / 100
interest_rate_float = interest_rate_float / 12
monthly_payment = home_price_float * (interest_rate_float * (1 + interest_rate_float) ** loan_length_float
                                      ) / ((1 + interest_rate_float) ** loan_length_float - 1)
monthly_payment_output = round(monthly_payment, 2)

# output
print("Your mortgage payment would be: $", monthly_payment_output, sep="")
