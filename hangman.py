import random
import time

wordbank = ["cat", "clock", "party", "sword", "butter", "tan", "pan", "utopia"]
goes_left = 10

print ("Hello! Let's play a game of hangman!")

word = random.choice(wordbank)
time.sleep(5)

while goes_left != 0:
    word_len = len(word)
    print ("""
    The word I'm thinking of has %d letters.
    You have 10 goes to guess letters.
    You can guess the word at any time.
    You have %d goes left!
    """ % (word_len, goes_left)
    )
    g_word = len(word) * "_ "
    print (g_word)
    guess_letter = input("Try to guess a letter!")
    guess_letter = guess_letter.lower()
    if len(guess_letter) != 1 or guess not in "abcdefghijklmnopqrstuvwxyz":
        print("That is not a letter, try again.")

    goes_left = goes_left -1
