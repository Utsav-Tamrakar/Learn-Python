#Optimized solution of all divisors
n=int(input("Enter a number: "))
i = 1
while i*i < n:
  if n%i==0:
    print(i)
    print(int(n/i))
  i+=1
if i*i==n:
  print(i)
  
  
#Optimized solution of all prime
n=int(input("Enter n: "))
if n<=1:
  print("No")
else:
  i=2
  while i*i <=n:
    if n%i==0:
      print("No")
      break
    i+=1
  else:
    print("Yes")