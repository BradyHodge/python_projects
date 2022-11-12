# Made by Brady Hodge
# CSE 110
# 08 Teach: Team Activity - Iterating Through Strings


user_fav_letter = input("What is your favorite letter? ").lower()
print(user_fav_letter)
word = "Commitment"
for i in word:
    if i == user_fav_letter:
        i = "_"
    else:
        i = i.lower()
    print(i, end="")