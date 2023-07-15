#  Number Guessing Game
import random

print("Number Guessing Game".center(50))

x=int(input("Enter Lower Number:- "))
y=int(input("Enter Upper Number:- "))
z=int(random.randint(x,y))

if y>=50:
    c = y // 10
else:
    c=5
n=0
print("Search Between",x,"and",y)
print("You Have Only",c,"Chances.")

while c>0:
    n=int(input("Enter Number:- "))
    if n==z:
        print("Congrats You Win..\nThe Number is:- ",z)
        break
    elif n>z:
        print("Your Number is Greater..\nTry Smaller Number.")
        c=c-1
        print("You Have",c,"Chances Left.")
    elif n<z:
        print("Your Number is Smaller..\nTry Bigger Number.")
        c=c-1
        print("You Have",c,"Chances Left.")

if c==0:
    print("You Loose..\nNumber is:-",z,"\nBetter Luck Next Time.")
