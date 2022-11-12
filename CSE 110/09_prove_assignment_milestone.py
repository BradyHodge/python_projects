# Made by Brady Hodge
# CSE 110
# 09 Prove: Assignment Milestone - shopping cart

# define variables
keep_going = True
cart = []
total = 0

# welcome the user
print("Welcome to the Shopping Cart Program!")

# main loop
while keep_going:
    # get user input
    print("\nPlease select one of the following")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    user_choice = input("Please ent an action: ")

    if user_choice == "1":
        # add item to cart
        item = input("What item would you like to add? ")
        cart.append(item)
        print(f"'{item}' added to cart")

    elif user_choice == "2":
        # view cart
        print("Your cart contains:")
        for item in cart:
            print(item)

    elif user_choice == "3":
        # remove item from cart
        item = input("What item would you like to remove? ")
        cart.remove(item)
        print(f"'{item}' removed from cart")

    elif user_choice == "4":
        # compute total
        print("")

    elif user_choice == "5":
        # quit
        keep_going = False
        print("Thank you. Goodbye.")

    else:
        # invalid input
        print("Invalid input. Please try again.")
        continue
