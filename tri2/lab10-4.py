# ----------------------
# Made by Brady Hodge
# Status: Done
# lab 10-4; 1/1
# ----------------------

def sum_of_squares(xs):
    square_sum = 0
    for var in xs:
        var **= 2
        square_sum += var
    return square_sum


print(sum_of_squares([2, 3, 4]))
