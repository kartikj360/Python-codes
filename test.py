import math
print("     *      ")
print("   * * *    ")
print("  * * * *   ")
print(" * * * * *  ")
print("  * * * *   ")
print("   * * *    ")
print("     *      ")

print("     1      ")
print("    232     ")
print("   34543    ")
print("  4567654   ")
print(" 567898765  ")

a =30
b=math.acosh(a)
print(b)
c=1.456
d=math.ceil(c)
print(d)
e=45
f=math.cos(e)
print(f)
g=16
h=math.isqrt(g)
print(h)
i=29.273
j=math.trunc(i)
print(j)

def triarea():
 a1=(int)(input("Enter the first side of the triangle"))
 a2=(int)(input("Enter the second side of the triangle"))
 a3=(int)(input("Enter the third side of the triangle"))
 if a1+a2>a3:
  s=((a1+a2+a3)/2)
  s1=s-a1
  s2=s-a2
  s3=s-a3
  ar=s*s1*s2*s3
  area=(math.sqrt(ar))
  print("Area of the triangle is ")
  print(area)
 else:
     print("This triangle is not possible to exist")
     
triarea()