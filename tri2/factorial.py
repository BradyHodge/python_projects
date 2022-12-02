# ----------------------
# Made by Brady Hodge
# Status: Graded
# factorial prob; 1/1
# ----------------------

def factorial(input_int):
    return 1 if (input_int == 1 or input_int == 0) else input_int * factorial(input_int - 1);


user_numb = int(input("What number would you like to turn into a factorial? "))

numb_fact = factorial(user_numb)
print("The factorial of {} is {}.".format(user_numb, numb_fact))
