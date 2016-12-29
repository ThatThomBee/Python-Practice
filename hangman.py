import random

wordbank = ["cat", "clock", "party", "sword", "butter"]

goes_left = 10

print ("Hello! Let's play a game of hangman!")

while goes_left != 0:
    word = random.choice(wordbank)
    print ("""
    I'm thinking of a word.
    The word has %d letters.
    Would you like to guess one? You have %d goes.
    You can guess the word at any time.
    You have %d goes left!
    """ % len(word), goes_left
    )

    goes_left = goes_left -1
