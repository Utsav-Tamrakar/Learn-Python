#Factorial in python
# n=int(input("Enter a number:"))
# count=1
# for i in range(2,n+1):
#   count=count*i
# print("Factorial is ",count)

#library function which make it look so easy
import math  
n=int(input("Enter a number: "))
result=math.factorial(n)
print("Factorial is ",result)