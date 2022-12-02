# ----------------------
# Made by Brady Hodge
# Status: Done
# Assignment 9B; 2/2
# ----------------------
import equation_parts


def continue_loop():
    """Runs the program for as long as the user likes"""
    valid_input = False
    while not valid_input:
        keep_going = input("Do you want to continue? ")
        if keep_going.lower() == "y" or keep_going.lower() == "yes":
            con = True
            valid_input = True
        elif keep_going.lower() == "n" or keep_going.lower() == "no":
            con = False
            valid_input = True
        else:
            print("That is not an accepted value.\nPlease input yes or no.")
            valid_input = False
    return con


keep_going = True

# gets equation from the user
while keep_going:
    str_equation = str(input("Enter the equation. "))
    numb_word1 = ""
    math_op = ""
    numb_word2 = ""
    capture_first = True

# sorts the equation so it can be used in the function get_math_answer
    for let in str_equation:
        if equation_parts.is_numeric(let):
            if capture_first:
                numb_word1 += let

            else:
                numb_word2 += let

        elif equation_parts.is_math_symbol(let):
            math_op = let
            capture_first = False

# gets the answer and prints an output
    ans = equation_parts.get_math_answer(numb_word1, math_op, numb_word2)
    print("{} {} {} = {}".format(numb_word1, math_op, numb_word2, ans))
    keep_going = continue_loop()
