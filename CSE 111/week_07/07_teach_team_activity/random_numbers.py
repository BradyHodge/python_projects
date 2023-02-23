"""
Made by Brady Hodge
CSE 111
07 Teach Team Activity: Lits
"""

import random

def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)

    words = []
    append_random_words(words)
    print(words)
    append_random_words(words, 5)
    print(words)

def append_random_numbers(numbers, quantity=1):
    for _ in range(quantity):
        numbers.append(round(random.uniform(0, 100), 1))

def append_random_words(words_list, quantity=1):
    for _ in range(quantity):
        words_list.append(random.choice(["the", "a", "one", "some", "many"]))

if __name__ == "__main__":
    main()