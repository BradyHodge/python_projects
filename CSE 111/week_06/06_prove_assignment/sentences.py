"""
Made by Brady Hodge
CSE 111
06 Prove Assignment: Troubleshooting Functions
"""

import random



def main():
    """Generate and print a sentence.
    """
    for _ in range(6):
        quantity = random.randint(1, 2)
        tense = random.choice(["past", "present", "future"])
        print_sentence(quantity, tense)


def print_sentence(quantity, tense):
    """Print a sentence with the given quantity and tense.
    A sentence is a determiner, a noun, a verb, and a period.
    The determiner and noun will agree in number (singular or plural).
    The verb will agree in number and person (1st, 2nd, or 3rd).

    Parameters
        quantity: an integer that determines if the noun
            is singular or plural.
        tense: a string that determines if the verb is
            past, present, or future.
    """
    determiner = get_determiner(quantity)
    verb = get_verb(quantity, tense)
    noun = get_noun(quantity)
    prepositional_phrase = get_prepositional_phrase(quantity)
    adjective = get_adjective()

    # Print the sentence.
    print(determiner.capitalize(), adjective, noun, verb, prepositional_phrase + ".\n")



def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if  quantity == 1:
        words = [ "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a noun.
    word = random.choice(words)
    return word


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
                "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
                "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
                "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
                "will think", "will run", "will sleep", "will talk",
                "will walk", "will write"]

    # Randomly choose and return a verb.
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    # Build and return a prepositional phrase.
    phrase = preposition + " " + determiner + " " + noun
    return phrase


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    words = ["about", "above", "across", "after", "along",
            "around", "at", "before", "behind", "below",
            "beyond", "by", "despite", "except", "for",
            "from", "in", "into", "near", "of",
            "off", "on", "onto", "out", "over",
            "past", "to", "under", "with", "without"]

    # Randomly choose and return a preposition.
    word = random.choice(words)
    return word

def get_adjective():
    words = ["beautiful", "big", "bored", "busy", "crazy",
            "cute", "dark", "drunk", "dumb", "fat",
            "funny", "happy", "hungry", "interesting", "lazy",
            "little", "mean", "nervous", "nice", "old",
            "pretty", "sad", "scary", "short", "silly",
            "sleepy", "small", "stupid", "tall", "ugly",
            "weird"]

    # Randomly choose and return an adjective.
    word = random.choice(words)
    return word


if __name__ == "__main__":
    main()