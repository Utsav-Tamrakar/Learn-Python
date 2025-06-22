#GCD PROBLEM:taking two input numbers we need to find is large number which can divide both number
import math
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
# small=min(a,b)
# for i in range(1,small+1):
#   if(a%i==0 and b%i==0):
#     gcd = i
# print("GCD is ",gcd)
gcd=math.gcd(a,b)
print("GCD is ",gcd)