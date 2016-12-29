import random

var = 1

while var == 1:
    input('Press enter to roll the dice...')
    print (random.randint(1,6))
    goAgain = input('Would you like to roll again? Y/N...')
    if goAgain[0] == 'N':
        var = 2
        print('Goodbye')
