count = 2
pfn = 600851475143
primeList = []

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

while count < pfn:
   if isPrime(count) and (pfn%count == 0):
      primeList.append(count)

      product = 1
      for e in primeList:
         product *= e

      if product == pfn:
         print primeList
         break

   count += 1


