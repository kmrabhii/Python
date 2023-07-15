import time

t=time.strftime('%T')
h=int(time.strftime('%H'))
m=int(time.strftime('%M'))

# h=int(input("Enter H"))
# m=int(input("Enter M"))

print(t)

if h>6 and h<12:
    print("Good Morning Sir".center(50))
    exit()
elif h==6:
    if m>=0:
        print("Good Morning Sir".center(50))
        exit()
elif h>12 and h<16:
    print("Good Afternoon Sir".center(50))
    exit()
elif h==12:
    if m>=0:
        print("Good Afternoon Sir".center(50))
        exit()
elif h>16 and h<20:
    print("Good Evening Sir".center(50))
    exit()
elif h==16:
    if m>=0:
        print("Good Evening Sir".center(50))
        exit()
elif h>20 and h<=23:
    print("Good Night Sir".center(50))
    exit()
else:
    print("Good Night Sir".center(50))