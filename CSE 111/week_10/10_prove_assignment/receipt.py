"""
Made by Brady Hodge
CSE 111
10 Prove Assignment: Handling Exceptions
"""

def main():
    """Calls the read_dictionary function and stores the compound dictionary in a variable named products_dict.
Prints the products_dict.
Opens the request.csv file for reading.
Skips the first line of the request.csv file because the first line contains column headings.
Uses a loop that reads and processes each row from the request.csv file. Within the body of the loop, your program must do the following for each row:
Use the requested product number to find the corresponding item in the products_dict.
Print the product name, requested quantity, and product price."""

    try:
        products_dict = read_dictionary("products.csv", 0)
        numb_of_items = 0
        subtotal = 0
        with open("request.csv", "r") as file:
            next(file)
            print_header()
            for line in file:
                line = line.strip()
                line = line.split(",")
                product_number = line[0]
                requested_quantity = line[1]
                product_name = products_dict[product_number][1]
                product_price = products_dict[product_number][2]
                numb_of_items += int(requested_quantity)
                subtotal += float(product_price) * int(requested_quantity)
                print(f"{product_name} {requested_quantity} @ ${product_price}")
            
            print(f"\nNumber of items: {numb_of_items}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Sales Tax: ${get_sales_tax_amount(subtotal):.2f}")
            print(f"Total: ${get_total_amount_due(subtotal, get_sales_tax_amount(subtotal)):.2f}")
            print_footer("request.csv", products_dict)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    except KeyError:
        print(f"Error: unknown product ID in the csv file \"{product_number}\"")
    

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, "r") as file:
        next(file)
        for line in file:
            line = line.strip()
            line = line.split(",")
            key = line[key_column_index]
            dictionary[key] = line
    return dictionary

def get_current_date_and_time():
    """Return the current date and time as a string."""
    import datetime
    now = datetime.datetime.now()
    return now.strftime("%a %b %d, %H:%M:%S, %Y")

def get_sales_tax_amount(subtotal):
    """Return the sales tax amount for the given subtotal."""
    sales_tax_rate = 0.06
    return subtotal * sales_tax_rate

def get_total_amount_due(subtotal, sales_tax_amount):
    """Return the total amount due for the given subtotal and sales tax amount."""
    return subtotal + sales_tax_amount

def print_header():
    """Print the header for the receipt."""
    print("Inkom emprium\n")

def print_footer(filename, products_dict):
    """Print the footer for the receipt."""
    print(f"\nThank you for shopping at Inkom Emprium!")
    print(get_current_date_and_time())
    get_coupon(filename, products_dict)
    print("We love feedback! Take a survey at www.inkomemprium.com/survey")

def get_coupon(filename, products_dict):
    """Prints a coupon for the customer."""
    import random
    item_list = []
    with open(filename, "r") as file:
        next(file)
        for line in file:
            line = line.strip()
            line = line.split(",")
            product_number = line[0]
            item_list.append(product_number)
    coupon_list = ["10% off your next purchase", "20% off your next purchase", "30% off your next purchase", "40% off your next purchase", "50% off your next purchase"]
    print(f"\nYour coupon is: {random.choice(coupon_list)} of {products_dict[random.choice(item_list)][1]}!")

if __name__ == "__main__":
    main()