#Palindrome problem

s=input("Enter a string to check a palindrome: ")
low=0
high=len(s)-1
while low<high:
   if s[low]!=s[high]:
     print("No")
     break
   low=low+1
   high=high-1
else:
  print("Yes")
  
  
#Shortcut method
s=input("Enter a string to check a palindrome: ")
if s==s[::-1]:
  print("Yes")
else:
  print("No")