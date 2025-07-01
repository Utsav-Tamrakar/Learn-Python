#Find the first digit
def fun(x):
  while x>=10:
    x=x//10
  return x

x=int(input("Enter the number: "))
print(fun(x))


#Another method using logarthmic
import math
def getFirstDigit(x):
  d=int(math.log10(x))
  res=x//(10**d)
  return res

x=int(input("Enter value of x: "))
print(getFirstDigit(x))