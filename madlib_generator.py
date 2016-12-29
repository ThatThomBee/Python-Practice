#MadLib generator. The user gives us the nouns, verbs and other stuff, and the computer generates a MadLib.
#Window Size
import os
os.environ['LINES'] = "90"
os.environ['COLUMNS'] = "160"

#Variable for the loop
mad_lib = 1

print ("Let's generate some silly shit together. Press enter to continue.")
print ("Let's start with you telling me your name.")
Name = input() #The users name
intro_text = """
    Nice to meet you %s!
    I'm going to go all Professor Oak on you now...
    are you a BOY or a GIRL?
    Or anything in between...I don't really care, gender is a construct
""" % Name
print (intro_text)

gender = input() #User's gender

pronoun = Name
if len(gender) > 0:
    gender = gender.lower()
    if gender == "boy":
        pronoun = "He"
    elif gender == "girl":
        pronoun = "She"
    else:
        pronoun = Name

#Let's start the loop here so we can remember the users name and gender
while mad_lib == 1:
    print ("OK %s give us a NOUN!" % Name)
    NounOne = input() #Our first noun
    print ("Let's be adventurous, give us anouther NOUN.")
    NounTwo = input () #Our second noun
    print ("OK, that's enough nouns. Why don't you try a VERB?")
    VerbOne = input() #Our first verb
    print ("One more VERB, just to be safe...")
    VerbTwo = input() #Our second verb
    print (
        "Not bad " + Name + ", how about one more VERB. \n"
        "This time, a VERB that ends in -ing.")
    VerbIng = input() #A verb ending in -ing, they've probably aleady done one of these, but that's their mistake not ours
    print ("Name a PLACE")
    Place = input() #Place name
    print ("I'll take an ADJECTIVE for 10 points!")
    AdjectOne = input() #Our first adjective
    print (
        "Sorry buddy, I lied, there's no points here. \n"
        "I will take another ADJECTIVE though.")
    AdjectTwo = input() #Our second adjective
    print (
        "Alright, name a PART OF YOUR BODY! Try not to be too rude... \n"
        "or do...what am I? Your mother?")
    BodyPart = input() #Body part...probably their dick, it's what I'd do
    print (
        "Speaking of your mother, have you called her recently? \n"
        "She misses you. Name a MEMBER OF YOUR FAMILY."
        )
    FamilyMember = input() #Family member. Remember to combine this and BodyPart. Because who doesn't want to see their grandma's name next to their junk?
    print ("OK " + Name + ", that should be everything. let's stick it all together.")

    #The MadLib part
    print (
        "There once was a " + gender + " called " + Name + ". \n"
        + pronoun + " was from the magical land of " + Place + ". \n"
        + Name + " had the most " + AdjectOne + " " + NounOne + ". \n"
        "But it wasn't as impressive as " + FamilyMember + " and their " + AdjectTwo + " " + BodyPart + ". \n"
        "In " + Place + " all there was to do was " + VerbOne + " and " + VerbTwo + "\n"
        "! Although sometimes " + Name + " could be spotted " + VerbIng + " with " + FamilyMember + ". \n"
        "THE END.....or is it? Would you like to go again " + Name + "? Press Y/N"
        )
    goAgain = input()

    #Go Again
    if goAgain[0] is "Y":
        mad_lib = 1

    elif goAgain[0] is "N":
        mad_lib = 0
        print ("Thankyou for playing, hopefully you weren't too filthy. Goodbye")
