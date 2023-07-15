#      Factorial

print("Factorial".center(50))


def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)


n = int(input("Enter a Number:- "))
print("Your Factorial is ", fact(n))
