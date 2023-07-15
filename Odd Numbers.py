# Print Odd Number From 1 to n

print("Print Odd Number From 1 to n.".center(50))


def odd(a):
    i = 0

    while True:
        i = i + 1
        if (i % 2 != 0):
            print(i)
            if (i > n):
                break
    print("Your Odd Numbers is Ready")


n = int(input("Enter The Number:- "))
odd(n)
