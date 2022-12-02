# Made by Brady Hodge
# CSE 110
# 12 Teach: Team Activity - Finding Items in a File

# define variables
largest_chapters = float("-inf")

book_of_interest = input("What volume of scriptures would you like to learn about? (for example, Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, Pearl of Great Price) ")

with open("books_and_chapters.txt") as f:
    for line in f:
        line = line.strip().split(":")

        # get the book, chapter and scripture
        book = line[0]
        chapter = int(line[1])
        scripture = line[2]

        if book_of_interest.lower() == book.lower():ch-
            if chapter > largest_chapters:
                largest_chapters = chapter
                largest_book = book
                largest_scripture = scripture

# print the largest book
try:
    print(f"The largest book is {largest_book} in the {largest_scripture} with {largest_chapters} chapters.")
except:
    print("That is not a valid book of scriptures.")