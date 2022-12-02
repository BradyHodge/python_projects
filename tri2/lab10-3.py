# ----------------------
# Made by Brady Hodge
# Status: Done
# lab 10-3; 1/1
# ----------------------

def max(list_of_ints):
    max_val = 0
    for var in list_of_ints:
        if var > max_val:
            max_val = var
        else:
            continue
    return max_val


print(max([10, 20, 35, 3, 8, 64, 23, 16, 44, 22]))
