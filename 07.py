n=1
count = 0

def isPrime(num):
   if((num%2!=0) and (num%3!=0)) or (num==2 or num==3):
      sqroot = num**0.5
      if long(sqroot) == sqroot:
         return False
      else:
         for i in range(4,int(sqroot)+1):
            if num%i == 0:
               return False
   else: 
      return False 
   return True

while count <= 10001:
   if isPrime(n):
      count += 1
   if isPrime(n) and count == 10001:
      print n
   n+=1


