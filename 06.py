sqsum = 0
sums = 0
for i in range(1,101):
   sqsum += i**2
   sums += i

print sums**2
print sqsum
print sums**2-sqsum
