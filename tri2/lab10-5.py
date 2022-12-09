# ----------------------
# Made by Brady Hodge
# Status: Done
# lab 10-5; 1/1
# ----------------------

def numb_of_odd(list_of_ints):
    count_odd = 0
    even_sum = 0
    for var in list_of_ints:
        if (var % 2) == 0:
            even_sum += var
        else:
            count_odd += 1
    return count_odd


print(numb_of_odd([10, 20, 35, 3, 8, 64, 23, 16, 44, 22]))
