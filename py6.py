
def hcf(a,b):
    c=0
    while(a%b!=0):
          c=a%b
          a=b 
          b=c

    return c

def lcm(a,b):
    gcd=hcf(a,b)
    LCM=((a*b)//gcd)
    return LCM





a=int(input("Enter the first no."))
b=int(input("Enter the second no."))

print("The hcf of the two no. is ",(hcf(a,b)))
print("The LCM of the two no. is ",(lcm(a,b)))