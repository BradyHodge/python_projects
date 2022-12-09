# compound interest

# explain the program to to the user
print("This program will find the compound interest of your loan.")

# assign variables and values
p = 10000
r = 0.08
n = 12

# ask the user for number of years
t = int(input("How many years is the loan?"))

# calculate the formula for interest
a = p*(1+(r/n))**(n*t)

# give the final amount after t years
print("After", " ", t, " ", "years, you will receive $", format(a, ".2f"), ".", sep="")
