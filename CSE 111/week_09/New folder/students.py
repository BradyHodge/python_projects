"""
Made by Brady Hodge
CSE 111
09 Team Activity: CSV Files
"""

import csv # Import the csv module to make reading the file easier.

def main():
    """Read the contents of a CSV file into a
    dictionary and print the dictionary.
    """
    filename = "students.csv" # The name of the CSV file.
    dictionary = read_dictionary(filename) # Use the read_dictionary function to make a dictionary of the file.
    keep_going = True # Start the loop.
    while keep_going == True:
        number = input("Enter a student number: ")
        number = number.replace("-", "") # Remove the dashes from the number.
        try: # Try to print the name of the student.
            print(f"The student's name is {dictionary[number]}"
            )
        except: # Print an error message based on the problem.
            if number.isnumeric() == False:
                print("Invalid I-Number. The I-Number must contain only digits.")
            elif len(number) != 9:
                print("The student number must be 9 digits long.")
            else:
                print("That student number is not in the file.")
        print()
        keep_going = input("Do you want to look up another student? (y/n) ") # Ask if the user wants to keep going.
        if keep_going.lower() == "y" or keep_going.lower() == "yes":
            keep_going = True # Keep the loop going.
        else:
            keep_going = False # End the loop.

def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file) # Create a CSV reader.
        next(reader) # Skip the header row.
        for row in reader: # Write each row to the dictionary.
            dictionary[row[0]] = row[1]
    return dictionary

if __name__ == "__main__": # Only run the main function if this file is run directly.
    main()