# A program to calculate the area of a shape given by the user.
# The user will specify a shape, and then define it's parameters.
# The program will calculate the area.
import time
import math

var = 1
while var == 1:
    print ("Let's see if we can figure out the area of a shape.")
    shape = input("""

    Is your shape a TRIANGLE, SQUARE or a CIRCLE?

    """)
    shape = shape.lower()

    if shape == "square":
        square_side = int(input("""

        What is the length of one side of your square in centimetres??
        Only type the number (e.g. 5cm will be written as 5.)

        """))
        s_area = square_side * square_side
        print ("The area of your %s is %d" % (shape, s_area))
        time.sleep(2)
        go_again = input("Would you like to go again? Y/N...")
        go_again = go_again.lower()
        if go_again == "n":
            var = 0
            print ("Goodbye!")

    elif shape == "triangle":
        tri_base = int(input("""

        What is the length of the base of your triangle in centimetres??
        Only type the number (e.g. 5cm will be written as 5.)

        """))
        tri_height = int(input("""

        What is the height of your triangle in centimetres??
        Only type the number (e.g. 5cm will be written as 5.)

        """))
        tri_area = (tri_base * tri_height)/2
        print ("The area of your %s is %dcm" % (shape, tri_area))
        time.sleep(2)
        go_again = input("Would you like to go again? Y/N...")
        go_again = go_again.lower()
        if go_again == "n":
            var = 0
            print ("Goodbye!")

    elif shape == "circle":
        cir_rad = int(input("""

        What is the radius of your circle in centimetres?
        Only type the number (e.g. 5cm will be written as 5.)

        """))
        cir_area = cir_rad * math.pi
        print ("The area of your %s is %dcm" % (shape, cir_area))
        time.sleep(2)
        go_again = input("Would you like to go again? Y/N...")
        go_again = go_again.lower()
        if go_again == "n":
            var = 0
            print ("Goodbye!")

    else:
        print ("""
        That was not a shape you could select.
        Please try again and read the instructions.
        """)
        time.sleep(2)
