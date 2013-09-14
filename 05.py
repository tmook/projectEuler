maxnum = 20
count = maxnum
found = False

while not found:
   for i in reversed(range(1,maxnum)):
      if count%i == 0:
         found = True
      else:
         found = False
         count +=maxnum
         break
print count
