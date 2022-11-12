# Made by Brady Hodge
# CSE 110
# 09 Teach Team Activity

# define vars
numb = ""
numbs = []
pos_numbs = []

# print instructions
print("Enter a list of numbers, type 0 when finished.")

# get numbers and append to list
while numb != 0:
    numb = int(input("Enter a number: "))
    numbs.append(numb)

# remove the last 0
numbs.remove(0)

# get the sum of the numbers
numbs_sum = sum(numbs)
print(f"The sum is : {numbs_sum}")

# get the average of the numbers
numbs_average = numbs_sum / len(numbs)
print(f"The average is : {numbs_average}")

# get the max of the numbers
numbs_max = max(numbs)
print(f"The largest number is : {numbs_max}")

# get the positive min of the numbers
for x in numbs:
    if x > 0:
        pos_numbs.append(x)
pos_numbs_min = min(pos_numbs)
print(f"The smallest positive number is : {pos_numbs_min}")

# sort the list
numbs_sort = numbs.sort()
print(f"The sorted list is : {numbs}")