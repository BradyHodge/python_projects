# program uses a loop to sum the cost of bottles of soda.

# variables
soda_cost = 2.73
cost = 0

# ask user for number of bottles
num_bottles = int(input("How many bottles of soda are you buying? "))

# for loop to sum the cost

for bottles in range(num_bottles):
    cost = cost + soda_cost

# add tax
cost_tax = cost *1.06

# rounding
cost = round(cost, 2)
cost_tax = round(cost_tax, 2)

# print the information for the user
print("The cost of the soda is $", format(cost, ".2f"), sep="")
print("The cost of soda with tax is $", cost_tax, sep="")
