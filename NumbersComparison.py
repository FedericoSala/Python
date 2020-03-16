import random
import sys

def compare(x,y):
    if x>y:
        print("Computer's number {} is bigger then yours {}".format(x,y))
    elif y>x:
        print("Your number {} is bigger then computer's {}".format(y,x))
    else:
        print("the numbers are equals")

computer = random.randint(1,100)

try:
    user = int(input("what's your integer number? "))
    if user > 100 or user<1:
        print("not a valid number")
    else: 
        compare(computer, user)
except ValueError:
    print("Not an integer value...")