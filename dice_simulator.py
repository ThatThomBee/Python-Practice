import random

var = 1

while var == 1:
    dice_face = input("""
    How many sides would you like your dice to have?
    You can use any number you want!
    """)
    #This was originally just a 6 sided sim, but added dice_face to create a more customisable sim.
    input('Press enter to roll the dice...')
    print (random.randint(1,int(dice_face)))
    goAgain = input('Would you like to roll again? Y/N...')
    goAgain = goAgain.lower()
    if goAgain[0] == 'n':
        var = 0
        print('Goodbye')
