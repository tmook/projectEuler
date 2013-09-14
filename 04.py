palStart = 100*100
palEnd = 999*999

lower = 100
upper = 999

def isPalindrom(palStr):
  palLen = len(palStr)
  for i in range(palLen):
    if palStr[i] != palStr[palLen-1-i]:
      return False
  return True

def getFactors(num,u,l):
  factorList = []
  for i in range(l,u+1):
    if palEnd%i==0:
      factorList.append(i)
  return factorList
    
limitCount=4;
while palEnd >= palStart:
  if isPalindrom(str(palEnd)):
    fList = getFactors(palEnd,upper,lower)
    if(len(fList) >= 2):
      for i in range(len(fList)):
        for j in range(len(fList)):
          if fList[i]*fList[j] == palEnd:
            print str(fList[i])+' * '+str(fList[j])+' = '+str(palEnd)
            limitCount -= 1
  palEnd -= 1
  if limitCount < 1:
    break;

