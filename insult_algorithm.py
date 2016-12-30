#A program to combine a swear word with an animal.
#Based on the Thom Bee theory of the perfect insult.
import random
import time
var = 1

foul_lan = [
"piss", "shit", "fuck", "cunt", "cock", "clunge", "shite", "jizz", "cum", "muff"
"panty", "minge", "wank", "trump", "bugger", "twat", "flap", "bum", "pussy", "sperm",
"fart"
]

animals = [
"weasel", "snail", "kitten", "fox", "pup", "slug", "monkey", "whale", "pigeon",
"fly", "falcoln", "hawk", "budgie", "ant", "womble"
]

while var == 1:
    print ("Let's receive a new insult to call your friends and nan.")
    time.sleep(2)
    swear = random.choice(foul_lan)
    suffix = random.choice(animals)
    print (swear + " " + suffix)
    time.sleep(2)
    go_again = input(
    """

    Would you like to go again? Y/N...

    """
    )
    go_again = go_again.lower
    if go_again()[0] is "n":
        var = 2
        print ("Fuckity-bye")
        time.sleep(3)
