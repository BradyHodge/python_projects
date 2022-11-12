# Made by Brady Hodge
# CSE 110
# 05 Prove: Milestone - Adventure Game

"""
+ added hidden "BACK" choice for "choice_1" for stretch goal
"""

# initial prompt
from tkinter import W


print("You slowly wake up, your head is throbbing. You can't remember where \
    you are and nothing around you looks familiar. It is extremely dark. It \
        appears like you are in and alleyway with massive buildings \
            surrounding you.")

# first choice
choice_0 = input(
    "Would you like to EXIT the alleyway or would you like to check \
        your POCKETS? ").upper()

# nested if statements to determine the path the user will take
if choice_0.strip() == "EXIT":
    print("You walk to the end of the alleyway as find yourself on the side \
        of an empty street. There is a group of people on the other side of \
            the street to your right.")
    choice_1 = input("Would you like to go to the GROUP or walk down the \
        STREET to the left? ").upper()
    if choice_1.strip() == "GROUP":
        print("You walk towards the group of people")
    elif choice_1.strip() == "STREET":
        print("You start walking down the street to the left, away from the \
            group.")
    elif choice_1.strip() == "BACK":
        print("You decide to go back to the alleyway.\
            \nYep is a dark alley, just like it was 30 seconds ago.\
            \nWhy did you walk back here?")

elif choice_0.strip() == "POCKETS":
    print("You check your pockets and find a phone and a key that you don't \
        recognize.")
else:
    print("I did not understand that, you can only pick options that are in \
        all caps. Example: EXIT")

    # You need to have at least three levels of scenarios with possible choices.

    # At least one of your scenarios must have more than two possible choices.

    # In each prompt, write the choices in ALL CAPS, so that the user knows which words are possible responses to choose.

    # When checking the users responses, you should match on the keyword, regardless of the uppercase/lowercase used in the response (e.g., "match", "MATCH", "Match" should all work).

    # Making different choices should take you to different scenarios. (You shouldn't have the same result for different choices.)

    # Choices should only work for the correct question.

    # In other words, if one scenario resulted in choices of Run/Hide, but another resulted in choices Follow/Look, you should not be able to respond with "Follow" to the question that asked for Run/Hide.

    # A good way to accomplish this is to have a series of nested if statements. (That is, the print and then the next if statement will be within the body/block of the first if statement.)

    # For each question, you should provide an "else" clause to handle the case that the user tries to type something other than the possible choices. It is up to you how to handle this case.

    # Showing Creativity and Exceeding Requirements
    # Obviously, you'll show creativity by customizing the prompts and choices. To achieve the grade category of "Shows creativity and exceeds requirements" for this one, you need to add something additional to the framework of the game. For example, you might add even more levels or you might have more choices at each level. You might add hidden choices or trick questions. Have fun with this and see what you can do!

    # If you've already learned other programming concepts (for example, loops, lists, etc.) you are welcome to use those concepts here as a way to make show creativity and exceed requirements.

    # Extra credit
    # For this assignment, you can earn +5 extra credit points by showing your program to at least two other people to have them play it. After they play it, briefly show them your code and explain how it works.

    # Milestone Requirements
    # At the end of Lesson 05, to help make sure you are on track to finish the assignment, you need to complete the following:

    # The program is working for the first question and possible choices, and displays a follow-up response to each choice (including an else condition).

    # For the milestone, you do not need to implement any additional scenarios/questions, you only need the first one.

    # Create a design for your complete game.

    # Prepare for the rest of your game by deciding on all the possible prompts, choices, and responses that the user might see. You should design the complete game, including else conditions. Then, to finish up the assignment for the next lesson, you'll just need to code up all of these options.

    # Feel free to write this design out on paper or in a document (Word, Google Docs, Powerpoint, etc.), whatever is most convenient for you. You should write each possible scenario along with its choices. Then, for each choice, write the resulting scenario with its choices, etc.

    # You are not required to submit this design to I-Learn, but you should complete it as part of your Milestone to make sure you are prepared to finish the program.
