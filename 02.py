first = 1
second = 2
next = 3

evenSum = 2

while next < 4000000:
  next = first + second
  if next%2 == 0:
    evenSum += next
  first = second
  second = next

print evenSum
