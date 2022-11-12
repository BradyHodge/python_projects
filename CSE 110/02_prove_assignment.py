# Made by Brady Hodge
# CSE 110
# 02 Prove: Assignment - Word Games

# welcome the user
print("Welcome to Word Games!\nPlease enter the following:\n")

# get input to user in the sentences
adjective_0 = input("adjective: ")
animal_0 = input("animal: ")
verb_0 = input("verb: ")
exclamation_0 = input("exclamation: ")
verb_1 = input("verb: ")
verb_2 = input("verb: ")

# added for stretch goal 
adjective_1 = input("adjective: ")
noun_0 = input("noun: ")
place_0 = input("place: ")
noun_1 = input("noun: ")

if noun_1[0] == "a" or  noun_1[0] == "e" or noun_1[0] == "i" or noun_1[0] == "o" or noun_1[0] == "u":
    a_or_an = "an"

else:
    a_or_an = "a"

# put everything together
print("Your story is:\n")
print(f"The other day, I was really in trouble. It all started when I saw a very {adjective_0} {animal_0} {verb_0} down the hallway. \"{exclamation_0.capitalize()}!\" I yelled. But all I could think to do was to {verb_1} over and over. Miraculously, that caused it to stop, but not before it tried to {verb_2} right in front of my family.")

# added for stretch goal 
print(
    f"\nI was {adjective_1}, looking out the sun-splashed window and sucking in deep breaths of {noun_0}. I didn't know what to do. I never imagined I'd have to deal with anything like that. This was nothing like that one time in {place_0}. I knew I had to do something, but I didn't know what, or how I could possibly handle it. I turned to my left and that is when I saw it! It was {a_or_an} {noun_1}!")
