import math

def Cos(a,n):
    Sum=1
    sign=-1
    for i in range(2,n,2):
        fact=math.factorial(i)
        print(fact)
        Pow=pow(a,i)
        print(Pow)
        Sum=Sum + sign*(Pow/fact)
        print(Sum)
        sign*=-1

    return float(Sum)

def series(a,n):
    Sum=1
    for i in range(2,n,2):
        fact=math.factorial(i)
        Pow=pow(a,i)
        Sum=Sum + Pow/fact

    return float(Sum)


a=int(input("Enter the no. whos series is to be found: "))
n=int(input("Enter the value of n: "))
c=Cos(a,n)
s=series(a,n)
print("The value of cos series is : ",c)
print("The value of the next series is : ",s)