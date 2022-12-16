
r1=int(input("Enter the no. of rows in 1st list: "))
r2=int(input("Enter the no. of rows in 2nd list: "))
c1=int(input("Enter the no. of cols in 1st list: "))
c2=int(input("Enter the no. of cols in 2nd list: "))

a=[]
b=[]

print("Lets enter the value in the 1st list")
for i in(0,r1,1):
    k=[]
    for j in(0,c1,1):
        print("Enter the value in ",i,"row",j,"column:")
        x=int(input())
        k.append(x)
        # print(k)
    a.append(k)
    # print(a)
print("Lets enter the valu in the 2nd list")
for i in(0,r2,1):
    l=[]
    for j in(0,c2,1):
        print("Enter the value in ",i,"row",j,"column:")
        y=int(input())
        l.append(y)
        # print(l)
    b.append(l)
    # print(b)

print("lets display  the 1st list")
i=0
for i in (a):
    print(i)

# i=0
# j=0
# for i in(a):    
#         for j in (i):
#          print(j,end=" ")
#         print("\n")    
# i=0
# j=0    
print(a)
print(b)
print("lets display  the 2nd list")
i=0
for i in(b):
    print(i)
# for i in(b):
#     for j in (i):
#         print(j,end=" ")
#     print("\n")    
print('Now lets add the two matrixes:')
result=[]
for i in(0,r1):
    for j in (0,c1):
        result[i][j]=a[i][j]+b[i][j]

i=0
for i in(result):
    print(i)
