print("This game is Guess my Number. Try to pick the number I have guess between 1 and 10.")

number = 5
for x in range(1, 6):
    guess = int(input("Guess a number between 1 and 10 "))
    print(number == guess)
    print(5 - x, "guesses remaining")
