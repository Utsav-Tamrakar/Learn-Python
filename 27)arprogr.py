#Arthimetic Progression nth term in python
#nth term =a+(n-1)d, a = first term, d= common difference, n =term number
# a=5
# d=3
# n=10
# print("The {}th term of the arithmetic progression is: {}".format(n, a + (n - 1) * d))
a=int(input("Enter a:"))
d=int(input("Enter d:"))
n=int(input("Enter n:"))
result=a+(n-1)*d
print(result)

#Geometric Progression nth term in python
#nth term =a*(r**(n-1)), a = first term, r= common ratio, n =term number
a=int(input("Enter a:"))
r=int(input("Enter r:"))
n=int(input("Enter n:"))
result=a*(r**(n-1))
print(result)