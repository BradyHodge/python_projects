"""
Made by Brady Hodge
CSE 111
09 Prove Milestone: Text FIles
"""

def main():
    """"""

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
    # Open the file for reading.
    infile = open(filename, 'r')

    # Read the first line of the file.
    line = infile.readline()

    # Initialize the dictionary.
    dictionary = {}

    # Read the rest of the lines in the file.
    while line != '':
        # Strip the newline character from the line.
        line = line.rstrip('\n')

        # Split the line into a list of strings.
        line_list = line.split(',')

        # Get the key.
        key = line_list[key_column_index]

        # Get the value.
        value = line_list[:key_column_index] + \
            line_list[key_column_index + 1:]

        # Add the key and value to the dictionary.
        dictionary[key] = value

        # Read the next line.
        line = infile.readline()

    # Close the file.
    infile.close()

    # Return the dictionary.
    return dictionary

if __name__ == '__main__':
    main()