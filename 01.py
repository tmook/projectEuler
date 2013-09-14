totalSum = 0
maxNum = 1000

for i in range (1,maxNum):
   if (i%3==0) or (i%5==0):
      totalSum += i

print totalSum
