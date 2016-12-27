#MadLib generator. The user gives us the nouns, verbs and other stuff, and the computer generates a MadLib.
#Window Size
import os
os.environ['LINES'] = "90"
os.environ['COLUMNS'] = "160"

#Variable for the loop
MadLib = 1 

print ("Let's generate some silly shit together. Press enter to continue.")
print ("Let's start with you telling me your name.")
Name = raw_input() #The users name
print ("Nice to meet you " + Name + ", I'm going to go all Professor Oak on you now...are you a BOY or a GIRL? Or anything in between...I don't really care, gender is a construct.")
Gender = raw_input() #User's gender

#Let's start the loop here so we can remember the users name and gender
while MadLib == 1:
    print ("OK " + Name + ",give us a NOUN!")
    NounOne = raw_input() #Our first noun
    print ("Let's be adventurous, give us anouther NOUN.")
    NounTwo = raw_input () #Our second noun
    print ("OK, that's enough nouns. Why don't you try a VERB?")
    VerbOne = raw_input() #Our first verb
    print ("One more VERB, just to be safe...")
    VerbTwo = raw_input() #Our second verb
    print ("Not bad " + Name + ", how about one more VERB. This time, a VERB that ends in -ing.")
    VerbIng = raw_input() #A verb ending in -ing, they've probably aleady done one of these, but that's their mistake not ours
    print ("Name a PLACE")
    Place = raw_input() #Place name
    print ("I'll take an ADJECTIVE for 10 points!")
    AdjectOne = raw_input() #Our first adjective
    print ("Sorry buddy, I lied, there's no points here. I will take another ADJECTIVE though.")
    AdjectTwo = raw_input() #Our second adjective
    print ("Alright, name a PART OF YOUR BODY! Try not to be too rude...or do...what am I? Your mother?")
    BodyPart = raw_input() #Body part...probably their dick, it's what I'd do
    print ("Speaking of your mother, have you called her recently? She misses you. Name a MEMBER OF YOUR FAMILY.")
    FamilyMember = raw_input() #Family member. Remember to combine this and BodyPart. Because who doesn't want to see their grandma's name next to their junk?
    print ("OK " + Name + ", that should be everything. let's stick it all together.")
    
    #The MadLib part
    print ("There once was a " + Gender + " called " + Name + ". They were from the magical land of " + Place + ".")
    print (Name + " had the most " + AdjectOne + " " + NounOne + ". But it wasn't as impressive as " + FamilyMember + " and their " + AdjectTwo + " " + BodyPart)
    print ("in " + Place + " all there was to do was " + VerbOne + " and " + VerbTwo + "! Although sometimes " + Name + " could be spotted " + VerbIng + " with " + FamilyMember + ".")
    print ("THE END.....or is it? Would you like to go again " + Name + "? Press Y/N")
    goAgain = raw_input()

    #Go Again
    if goAgain[0] is "Y":
        MadLib = 1

    elif goAgain[0] is "N":
        MadLib = 0
        print ("Thankyou for playing, hopefully you weren't too filthy. Goodbye")


