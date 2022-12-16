def common(a,b):
  size1=len(a)
  size2=len(b)
  c=a[1:-1].split()
  d=b[1:-1].split()
  count=0
  size1=len(c)
  size2=len(d)
  for i in range(0,size1-1):
    i=+1    
    for j in range(0,size2-1):
     if(c[i]==d[j]):
         count=count+1
         j=+1
     else:
         j=+1    
  print("The number of common character in both the string is")
  print(count)     
      
a=str(input("Enter the 1st string"))
b=str(input("Enter the 2nd string"))
common(a,b)   