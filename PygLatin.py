pyg = 'ay'
var = 1

while var == 1:
    original = input('Enter a word:  ')
    if len(original) > 0 and original.isalpha():
        word = original.lower()
        first = word[0]
        new_word = word [1:len(word)] + first + pyg
        print (new_word)
        try_again = input('Would you like to go again? Y?N   ')
        if try_again is 'N':
            var = 2
            print ('Goodbye!')
    elif len(original) == 0:
        print ('You have not entered a word!   ')
    elif len(original) > 0 and original.isdigit():
        print ('Real words are not numbers! Try again.   ')
    elif original.isalpha() and original.isdigit():
        print ('Please type words, not passwords. No numbers!   ')
    else:
        print ('Try again!   ')
