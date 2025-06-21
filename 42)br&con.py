#Break and Continue in python\
  
#Break statement using for loop
n=int(input("Enter a number:"))
for i in range(2,n+1):
  if n % i == 0:
   print(i)
   break

#Break statement using while loop
n=int(input("Enter a number:"))
i=2
while i<=n:
  if n % i == 0:
    print(i)
    break
  i += 1
#example of break statement
i=1
while i<=5:
  if i == 3:
    break 
  print(i)
  i+=1
print(i)

#Continue statement : it doesn't execute the content after continue statement instead it goes to the next iteration of the loop
l=[10,16,17,18,45,50,60]
for i in l:
  if i % 5 == 0:
    continue
  print(i)
  
for i in l:
  if i % 2 != 0:
    print(i)
    
#Example of continue statement
i=0
while i<=5:
  if i==3:
    i=i+1
    continue
  print(i,i*i)
  i += 1