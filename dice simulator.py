import random

var = 1

while var == 1:
    raw_input('Press enter to roll the dice...')
    print (random.randint(1,6))
    goAgain = raw_input('Would you like to roll again? Y/N...')
    if goAgain[0] is 'N':
        var = 2
        print('Goodbye')
