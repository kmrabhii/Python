#  Number Guessing Game
import random

print("Number Guessing Game".center(50))


x=int(input("Enter First Number:- "))
y=int(input("Enter Second Number:- "))
z=int(random.randint(x,y))

c=12
n=0
print("You Have Only",c,"Chances.")

while c>0:
    n=int(input("Enter Number:- "))
    if n==z:
        print("Congrats You Win..")
        break
    elif n>z:
        print("Your Number is Greater..")
        c=c-1
        print("You Have ",c,"Chances Left")
    elif n<z:
        print("Your Number is Smaller..")
        c=c-1
        print("You Have ",c,"Chances Left")

if c==0:
    print("You Loose..\nBetter Luck Next Time.")
