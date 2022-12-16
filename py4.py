def reverse(num):
 sum=0
 a=num
 rev=0
 remd=0
 while(a>0):
   remd=a%10
   sum=sum+remd
   rev=(rev*10)+remd
   a=a//10
 print("Your number after being reversesd")
 print(rev)
 print("The Sum of all the digits")
 print(sum)
 
num=int(input("Enter the number to be reversed"))
reverse(num)
 