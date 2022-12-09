# Made by Brady Hodge
# CSE 110
# 10 Teach: Team Activity - Multiple Lists

# define variables
keep_going = True
names = []
balances = []
total = 0
average = 0
highest_balance = 0


# print instructions
print("\nEnter the names and balances of bank accounts (type: quit when done)")

# loop untell the user quits
while keep_going:
    # get user input
    name = input("Enter the name of the account: ")
    if name == "quit":
        keep_going = False
        break
    balance = float(input("Enter the balance of the account: "))
    if balance == "quit":
        keep_going = False
        break

    # add the name and balance to the lists
    names.append(name)
    balances.append(balance)
    

# print the names and balances
print("\nAccount Information:")
for i in range(len(names)):
    print(f"{i}. {names[i]} - ${balances[i]}")

    # calculate the total balance
    total += balances[i]

    # calculate the highest balance
    if balances[i] > highest_balance:
        highest_name = names[i]
        highest_balance = balances[i]


# calculate the average balance
average = total / len(names)
average = round(average, 2)

# print the total and average
print(f"\nTotal: ${total}")
print(f"Average: ${average}")
print(f"Highest balance: {highest_name} - ${highest_balance}")

keep_going = True

# loop untell the user quits
while keep_going:
    update = input("Do you want to update an account?(yes/no) ")
    if update == "yes":
        # get the account number
        account_number = int(input("What account index do you want to update: "))
        # get the new balance
        new_balance = float(input("Enter the new balance: "))
        # update the balance
        balances[account_number] = new_balance
        # print the names and balances
        print("\nAccount Information:")
        for i in range(len(names)):
            print(f"{i}. {names[i]} - ${balances[i]}")
    elif update == "no":
        keep_going = False
        break
    else:
        print("Invalid input. Please try again.")
        continue