# Made by Brady Hodge
# CSE 110
# 10 Prove: Assignment - shopping cart

"""
+ added formatting to aline prices
+ added the tax to the total
"""

# define variables
keep_going = True
cart = []
prices = []
total = 0

# welcome the user
print("Welcome to the Shopping Cart Program!")

# main loop
while keep_going:
    # get user input
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    user_choice = input("Please enter an action: ")

    # add item to cart
    if user_choice == "1":
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item}'? "))
        prices.append(price)
        cart.append(item)
        print(f"'{item}' added to cart")


    # view cart
    elif user_choice == "2":
        print("Your cart contains:")
        for i in range(len(cart)):
            # add 1 to i to show the user the first item as 1 instead of 0
            print(f"{i + 1}. {cart[i]:<15}  ${prices[i]:.2f}")

    # remove item from cart
    elif user_choice == "3":
        # check if there is anything in the cart
        if len(cart) == 0:
            print("Your cart is empty!")
        else:
            # remove item from cart
            item = int(input("What item would you like to remove? "))
            # subtract 1 to index to show the user the first item as 1 instead of 0
            item -= 1
            cart.pop(item)
            prices.pop(item)
            print(f"'{item + 1}' removed from cart")

    # compute total
    elif user_choice == "4":
        for item in cart:
            total += prices[cart.index(item)]
        sales_tax = float(input("What is the sales tax rate? "))
        total += (sales_tax / 100) * total
        print(f"Total: ${total:.2f}")
        
    # quit
    elif user_choice == "5":
        keep_going = False
        print("Thank you. Goodbye.")

    else:
        # invalid input
        print("Invalid input. Please try again.")
        continue
