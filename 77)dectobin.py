# Decimal to binary in python
def decToBin(n):
  if n==0:
    return "0"
  res=""
  while n>0:
    res=res+str(n%2)
    n=n//2
  return res[::-1]