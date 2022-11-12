# ----------------------
# Made by Brady Hodge
# Status: In Progress
# Assignment 9A; 2/2
# ----------------------

import crypt_maker

# prompt the user for the text to encrypt.
user_text = str(input("What do you wish to encrypt? "))

# Prompt the user for an integer-based key.
user_key = int(input("What is the key? "))

# get both the Caesar and Rolling cipher results.
caesar_enc = crypt_maker.caesar(user_text, user_key)
roll_enc = crypt_maker.encrypt(user_text, user_key)

# use module to decrypt each of the results
caesar_dec = crypt_maker.caesar_back(caesar_enc, user_key)
roll_dec = crypt_maker.decrypt(roll_enc, user_key)

# Display all of these results to the user nicely formatted.
print(" Caesar     |   Rolling\n--------    |   --------\n {:^}    |   {:^}\n--------    |   --------".format(caesar_enc, roll_enc))
print(" {:^}    |   {:^}".format(caesar_dec, roll_dec))
