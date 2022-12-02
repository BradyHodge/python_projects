# Made by Brady Hodge
# CSE 110
# 11 Prepare: Checkpoint - books

# Open the file.
with open("books.txt") as book_file:

    # Go through each line in the file, one by one
    for line in book_file:
        # Remove the newline character from the end of the line.
        book = line.strip()

        # Print the book out to the screen
        print(book)