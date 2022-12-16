def check(a,b):
    flag=0
    for i in (a):
        for j in (b):
            if i==j:
                flag+=1
                break

    if flag==0:
        return -1
    else:
        return flag

a=input("Enter the First string: ")
b=input("Enter the second string: ")
c=check(a,b)
if c==-1:
    print("Both the strings have no character common")                    
else:
    print("The no. of common characters are :",c)
