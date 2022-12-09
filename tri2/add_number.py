# ----------------------
# Made by Brady Hodge
# Status: Done
# Date Started: 29/3/22
# ----------------------

# add number with user input

numbers_to_add = int(input("How many numbers do you want me to add? "))

sum = 0
i = 1

while i <= numbers_to_add:
    number = int(input("Enter a number: "))
    sum += number
    i += 1

print("The sum is " + str(sum))

