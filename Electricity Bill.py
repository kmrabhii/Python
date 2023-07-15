# Electricity Bill Calculator

print("Electricity Bill Calculator".center(50))
u=int(input("Enter The Number of Units:- "))

if u<=100:
    print("You Don't Need You Pay Any Ammount")
elif u>100 and u<=200:
    print("You Need to Pay",u*5,"Rupees")
else:
    print("You Need to Pay",u*10,"Rupees")