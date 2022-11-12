# ----------------------
# Made by Brady Hodge
# Status: In Progress
# Assignment 9A; 1/2
# ----------------------

import random


# Shifts letter the number of letter specified. This uses a straight forward approach.
def shift_letter(letter: str, shift: int) -> str:
    """get the minimum value of letters"""
    let_a = ord("a")
    """Adjust for capitals"""
    if "A" <= letter <= "Z":
        let_a = ord("A")

    """get value of letter with minimum removed"""
    ascii = ord(letter) - let_a
    new_ascii = (ascii + shift) % 26
    """add minimum back to value so that it is back in range of letters."""
    new_ascii += let_a
    new_letter = chr(new_ascii)
    return new_letter


# Create a caesar cipher, shifting only letter based on the key.
def caesar(text: str, key: int) -> str:
    new_text = ""
    for ltr in text:
        if not ltr.isalpha():
            new_letter = ltr
        else:
            new_shift = key
            new_letter = shift_letter(ltr, new_shift)
        """add letter to string"""
        new_text += new_letter
    return new_text


# create a rolling cipher; the shift is increased by one for each letter we find
def rolling(text: str, key: int) -> str:
    new_text = ""
    roll = 0
    for ltr in text:
        if "a" <= ltr <= "z" or "A" <= ltr <= "Z":
            new_shift = key
            new_letter = shift_letter(ltr, roll + new_shift)
        else:
            new_letter = ltr

        new_text += new_letter
        roll += 1
    return new_text


# decrypt the caesar cipher by shifting all letter back instead of forward.
def caesar_back(text, key):
    return caesar(text, 26 - key)


# create a rolling cipher; the key is the seed for a random shift
def encrypt(text: str, key: int) -> str:
    random.seed(key)
    new_text = ""
    for ltr in text:
        if "a" <= ltr <= "z" or "A" <= ltr <= "Z":
            new_shift = random.randrange(26)
            new_letter = shift_letter(ltr, new_shift)
        else:
            new_letter = ltr

        new_text += new_letter
    return new_text


# decrypt the encryption by using the key to get the seed by shifting all letters back instead of forward.
def decrypt(text: str, key: int) -> str:
    random.seed(key)
    new_text = ""
    for ltr in text:
        if "a" <= ltr <= "z" or "A" <= ltr <= "Z":
            new_shift = 26 - random.randrange(26)
            new_letter = shift_letter(ltr, new_shift)
        else:
            new_letter = ltr

        new_text += new_letter
    return new_text