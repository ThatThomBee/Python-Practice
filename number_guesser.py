# Guess the number game. The aim is to guess the number that the computer generates
import random



def _guess_loop(my_name):
    number = random.randint(1, 100)
    guesses = 0
    print('Hi %s, I am thinking of a number between 1 and 100, try and guess it.' % my_name)
    #Guessing loop
    while guesses < 8:
        print ('Take a guess!')
        guess = input()
        guess = int(guess)

        guesses = guesses +1

        if guess > number:
            print ('Your guess is too high!')

        if guess < number:
            print ('Your guess is too low!')

        if guess == number:
            break
    if guess == number:
        print('Well done %s you have guessed the number in %d guesses!' % (my_name, guesses))
    else:
        print ('Nah mate! The number I was thinking of was %d.' % number )

if __name__ == "__main__":
    print ('Hello, what is your name?')
    my_name = input()
    go_again = True
    while go_again:
        _guess_loop(my_name)
        go_again = input('Go again? Y/N...')[0] is 'Y'
