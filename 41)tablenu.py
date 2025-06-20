#table using while loop
n=int(input("Enter a number to print its table: "))
i=1
while i <= 10:
  print(n,"x", i,"=", n*i)
  i += 1
  
#Upto certain number using while loop

n=int(input("Enter a number:"))
m=int(input("Enter the number upto which you need a table:"))
i=1
while i <= m:
  print(n,"x", i,"=",n*i)
  i+=1
  
#table using for loop
m=int(input("Enter a number to print its table: "))
for i in range(1,11):
  print(m,"x", i,"=", m*i)

#upto certain number using for loop
n=int(input("Enter a number for table:"))
m=int(input("Enter the number upto which you need a table:"))
i=1
for i in range(1,m+1):
  print(n,"x", i,"=",n*i)