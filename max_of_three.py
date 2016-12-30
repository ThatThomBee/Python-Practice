#A simple script which outputs the largest of 3 numbers given by the user.

a = int(input("Enter a number!"))
b = int(input("Enter a second number!"))
c = int(input("Enter a third number!"))

if b < a > c:
    print("%d is the biggest number!" % a)
elif a < b > c:
    print("%d is the biggest number!" % b)
else:
    print("%d is the biggest number!" % c)
