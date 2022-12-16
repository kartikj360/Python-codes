import math


def check_eligibility(n):
    if(n >= 29 or n <= 1):
        print("Sorry")
        return False
    else:
        y = int(math.sqrt(n))
        for i in range(2, y):
            if(n % i == 0):
                print("Sorry")
                return False

    print("Process for printing")
    return True


def displayPattern(n):
    if(check_eligibility(n)):
        idx = ord('A')
        for i in range(0, n):
            cs = chr(idx+i)
            for j in range(0, n-i-1):
                print(" ", end="")
            print(cs, end="")
            for j in range(0, 2*i-1):
                print("*", end="")
            if(i != 0):
                print(cs)
            else:
                print()
    else:
        print("Pattern Not Possible")


y = int(input("Enter the number : "))
displayPattern(y)
