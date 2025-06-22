#Find the divisor of a number
n=int(input("Enter a number: "))
#Using for loop
# for i in range(1,n+1):
#   if n%i==0:
#     print(i)

#Using while loop
i = 1
while i<=n:
  if n%i==0:
    print(i)
  i+=1