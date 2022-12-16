import math
def primecheck(a):
    b=int(math.isqrt(a))
    flag=0
    for i in (2,b+1):
        if a%i==0:
            flag=1
    if flag==0:
       return True
    else:
        return False   
    



a=int(input("Enter the no."))
print("Is the no. is prime:",primecheck(a))
