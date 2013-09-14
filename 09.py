# a < b < c
# a^2 + b^2 = c^2
# a + b + c = 1000
# a*b*c = ???

for a in range(1,1001):
   for b in range(a+1,1001):
      c = 1000.0 - a - b
      cSqrd = (a**2 + b**2)**0.5
      if c == cSqrd:
         print str(a)+' * '+str(b)+' * '+str(c)+ ' = '+str(a*b*c)
         break
