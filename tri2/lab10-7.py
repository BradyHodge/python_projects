# ----------------------
# Made by Brady Hodge
# Status: Done
# lab 10-7; 1/1
# ----------------------

def replace(s, old, new):
    fin_s = s.replace(old, new)
    return fin_s


s = 'I love spom! Spom is my favorite food.'
print(replace(s, 'om', 'am'))
