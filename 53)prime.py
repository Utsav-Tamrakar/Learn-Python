#checking for prime in python
n=int(input("Enter a number: "))
if(n <= 1):
  print("No")
else:
  for i in range(2, n):
    if (n % i == 0):
      print("No")
      break
  else:
    print("Yes")
      