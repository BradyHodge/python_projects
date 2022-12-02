# Made by Brady Hodge
# CSE 110
# 05 Prove: Assignment - Adventure Game

"""
+ added "takes_place" to determine a random nonexistent city for stretch goal
"""

# pick a random nonexistent city for the story to take place in
import random

cites = ["Shadyland", "Urban Blooms", "Pawningville", "Enclave City", 
        "Cremont", "Inception City", "Cyno City", "Ethos City", "Portico", 
        "Eutopia", "Sprawl City", "Clout City", "Lushly", "Networked City", 
        "Nexicity", "Landward", "Spillaluna", "Verbo City", "Athro City", 
        "Metromic", "Chosen City", "Auda City", "Stonewall", "Aeon City", 
        "Serenity", "Millicity", "Shreveport", "Fathom City", "Landywood", 
        "Bloomsbury", "Lavatown", "Exotopia", "Landlord Hill", "Pinnacle", 
        "Newfaux", "Tisra", "Boca Vista", "Fortuna", "Bloomscape", 
        "Diverse City"]

takes_place = random.choice(cites)

# initial prompt
print("You slowly wake up, your head is throbbing. You can't remember where"
"you are and nothing around you looks familiar. It is extremely dark. "
"It appears like you are in and alleyway with massive buildings "
"surrounding you.")

# first choice
choice_0 = input("Would you like to EXIT the alleyway or would you like to "
            "check your POCKETS? ").upper()

# nested if statements to determine the path the user will take
if choice_0.strip() == "EXIT":
    print("You walk to the end of the alleyway and find yourself on the side "
    "of an empty street. There is a group of people on the other side of the"
    " street to your right huddled around something that you can not see.")

    choice_1 = input("Would you like to go to the GROUP or walk down the "
                "STREET to the left? ").upper()

    if choice_1.strip() == "GROUP":
        print("You walk towards the group of people. As you get close to the "
        "group of people the one that is closetest to you turns around.  He "
        "is holding a large kitchen knife. You freeze in place getting ready "
        "to react. A deep grin appears on his face.")

        choice_2 = input("Would you like to ATTACK, RUN or WAIT? ").upper()

        if choice_2.strip() == "ATTACK":
            print("You rush the man holding the knife, he tries to say "
            "something to you but the adrenalin is making your heartbeat pound"
            " in your head. The knife falls to the ground as you knock him over,"
            " you stand up glancing at the rest of the group, getting ready "
            "to take them on. They look at you in shock. At this moment you "
            "notice that one of them is holding a half eaten cake "
            "You realize that you have made a huge mistake.")
            print("\nThe cops are called and they arrest you for attacking someone "
            "completely unprovoked, and on his birthday no less. They "
            f"questioned what you where doing in {takes_place}, but you don't"
            " have an answer for them. You have never even heard of this "
            "place. It is almost like you are in a different world...")
            print("\nEnding: Federal Prison?")
        
        elif choice_2.strip() == "RUN":
            print("You take off running down the street. The main yells "
            "something in your direction but you can't hear him. You keep "
            "running until your out of breath. The street and surrounding "
            "area look identical to the one that you just ran from. ")
            print("You stop to take a breath. A completely black "
            "car rolls up next to you and the back door opens. Someone one the "
            "inside of the car says \"Get in, its not safe here at night after "
            "all.\"")

            choice_3 = input("Wou you like to get IN or keep WALKING? ").upper()

            if choice_3.strip() == "IN":
                print("You get in the car and the door shuts. You can't see "
                "anything. Your eyes begin to get very heavy."
                "\nNext thing you know you wake up in a dark room. There are "
                "dark figures huddled in the corner. One turns to you. \"So you're "
                "up?\" The figure said looking at you. I was hard to see their "
                "face in the dark. You ask where you where, they reply \"In the "
                "underground of course. Where did you think you where going to "
                "end up when you got kidnaped? \n The aristocrats of the city "
                "take the homeless and make them fight for entertainment. Its not"
                " much of a secret, the cops either don't care or can't find the "
                "evidence to do anything about it. Where are you from if you mind "
                "I ask?\" \n\"Never heard of there... well, welcome to "
                f"{takes_place}. Guess I will see you in the ring.\"")
                print("\nEnding: Welcome to the Underground!")

            elif choice_3.strip() == "WALKING":
                print("You keep walking, the door closes and they drive away. "
                "After some time, what looks like a cop car rolls up next "
                f"to you. The side of the car says {takes_place} police. " 
                "The window rolls down and the officer asks you \"Are you"
                " ok?\" You began talking, it turns out that the officers sister "
                "works for a homeless shelter. They offer to take you there and "
                "in the morning drive you to anywhere you want to go. You "
                "don't accept and decide that you don't need help.")
                print("\nEnding: New City, Who This?")
            
            else:
                print("I did not understand that, you can only pick options that"
            " are in all caps. Example: IN")

        elif choice_2.strip() == "WAIT":
            print("You hesitate, and you lock eyes with him. Then he says"
            " \"Do you want some cake?\" Another member of the group turns around"
            "holding about half of a cake. The man explains \"We were celebrating"
            "my birthday and the pub kicked us out to close. We have to finish "
            "the cake because the uber shows up so we don't get cake all over "
            "their car.\"")
            print("You slowly get some cake, still watching the man with the "
            "man with the knife as you do. The group explains that you are in"
            f" {takes_place}. A place you have never heard of. You crash at "
            "their house and decide to figure out where you are and how you "
            "got there in the morning.")
            print("\nEnding: New BFFs!") 
        else:
            print("I did not understand that, you can only pick options that"
            " are in all caps. Example: ATTACK")


    elif choice_1.strip() == "STREET":
        print("You start walking down the street to the left, away from the "
        "group.")
    
    else:
        print("I did not understand that, you can only pick options that"
        " are in all caps. Example: GROUP")

elif choice_0.strip() == "POCKETS":
    print("You check your pockets and find your phone and a key that you don't "
    "recognize. Your phone has no signal and the battery is really low. You "
    "decide to place both back into your pocket and you walk to the end of "
    "the alleyway. You find yourself on the side of an empty street with not "
    "a person or car in sight.")

    choice_1 = input("Would you like to walk to the RIGHT or the LEFT? ").upper()

    if choice_1.strip() == "RIGHT":
        print("You take a right and start walking down the street. You keep "
        "walking until you see shadowy figure standing the the shadows wearing"
        " all black. There seams to be a strange purple glow coming from his "
        "face.")

        choice_2 = input("Would you like to walk up to the shadowy FIGURE or "
        "would you like to keep WALKING? ").upper()

        if choice_2.strip() == "FIGURE":
            print("You began to walk up to the figure. You notice that his "
            "eyes are the source of the glowing. They speak to you in a low "
            "gravelly voice: \"How have you been enjoying your trip to "
            f"{takes_place}?\" \nYou stare at them with a blank stare, unsure "
            "what to do.\"Cat got your tongue?\" they say in their unnatural "
            "voice. \"Fine, if you hate it so much here you can just go "
            "back.\" The dark figure snaps his fingers and everything goes "
            "dark. \nYou walk up in your own bed. You feel as if you have had"
            " a strange dream...")
            print("\nEnding: Back to Earth?")

        elif choice_2.strip() == "WALKING":
            print("You keep walking, after a bit you find a red box on the "
            "side of the road. There is a key hole in the front. You put the "
            "key from your pocket into the lock and turn it. You open the box "
            "to find a fish of some kind, looks to be either a salmon  or a "
            "herring. Strange. You leave the box and keep walking.")
            print("After some time, what looks like a cop car rolls up next "
            f"to you. The side of the car says {takes_place} police. " 
            "The window rolls down and the officer asks you \"Are you"
            " ok?\" You began talking, it turns out that the officers sister "
            "works for a homeless shelter. They offer to take you there and "
            "in the morning drive you to anywhere you want to go. You "
            "reluctantly accept.")
            print("\nEnding: A Friend in Blue.")
        
        else:
            print("I did not understand that, you can only pick options that"
            " are in all caps. Example: RIGHT")
    
    elif choice_1.strip() == "LEFT":
        print("You walk to the left. After a few minuets a completely black "
        "car rolls up next to you and the back door opens. Someone one the "
        "inside of the car says \"Get in, its not safe here at night after "
        "all.\"")

        choice_2 = input("Wou you like to get IN or keep WALKING? ").upper()

        if choice_2.strip() == "IN":
            print("You get in the car and the door shuts. You can't see "
            "anything. Your eyes begin to get very heavy."
            "\nNext thing you know you wake up in a dark room. There are "
            "dark figures huddled in the corner. One turns to you. \"So you're "
            "up?\" The figure said looking at you. I was hard to see their "
            "face in the dark. You ask where you where, they reply \"In the "
            "underground of course. Where did you think you where going to "
            "end up when you got kidnaped? \n The aristocrats of the city "
            "take the homeless and make them fight for entertainment. Its not"
            " much of a secret, the cops either don't care or can't find the "
            "evidence to do anything about it. Where are you from if you mind "
            "I ask?\" \n\"Never heard of there... well, welcome to "
            f"{takes_place}. Guess I will see you in the ring.\"")
            print("\nEnding: Welcome to the Underground!")

        elif choice_2.strip() == "WALKING":
            print("You keep walking, the door closes and they drive away. "
            "After some time, what looks like a cop car rolls up next "
            f"to you. The side of the car says {takes_place} police. " 
            "The window rolls down and the officer asks you \"Are you"
            " ok?\" You began talking, it turns out that the officers sister "
            "works for a homeless shelter. They offer to take you there and "
            "in the morning drive you to anywhere you want to go. You "
            "don't accept and decide that you don't need help.")
            print("\nEnding: New City, Who This?")
        
        else:
            print("I did not understand that, you can only pick options that"
        " are in all caps. Example: IN")
    else:
        print("I did not understand that, you can only pick options that"
        " are in all caps. Example: RIGHT")

else:
    print("I did not understand that, you can only pick options that are in "
    "all caps. Example: EXIT")
