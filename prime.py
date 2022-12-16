import math
# checking for prime
def is_prime(n):
   if n <= 1:
      return False
   else:
      # iterating loop till square root of n
      for i in range(2, int(math.sqrt(n)) + 1):
         # checking for factor
         if n % i == 0:
            # return False
            return False
      # returning True
      return True
num=int(input("Enter the number:"))
print(is_prime(num))