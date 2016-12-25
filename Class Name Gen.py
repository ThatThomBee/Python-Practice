import random
var = 2

names = ['Dylan', 'Alexa', 'Jacob B', 'Milly', 'Jacob C', 'Raeya', 'Olly', 'Harry', 'Lilyrose', 'Brodie', 'Scarlett', 'Trae', 'Lexie', 'Grace', 'Dayley', 'Mia', 'Baby-Katrina', 'Maisie', 'Ellie P', 'Louise', 'Ellie R', 'Noah', 'Violet', 'Leo', 'Alfie', 'Louie', 'Peter', 'Isabelle', 'Lily']

select = raw_input('Choose a child? Y or N?     ')
while var == 2:
    if select[0] is 'Y':
        print(random.choice(names))
        go_again = raw_input('Choose again? Y or N?     ')
        if go_again[0] is 'N':
            var = 1
            print('Goodbye')
    elif select[0] is 'N':
        var = 1
        print('Goodbye')
