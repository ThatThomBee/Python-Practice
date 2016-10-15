pyg = 'ay'

original = raw_input('Enter a word:')
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word [1:len(word)] + first + pyg 
    print new_word
elif len(original) == 0:
    print 'You have not entered a word!'
elif len(original) > 0 and original.isdigit():
    print 'Real words are not numbers! Try again.'
else:
    print 'Try again!'
