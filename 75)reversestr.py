#Reverse string in python
#Strings in python are immutable...
s=input("Enter a string:")
rev=""
for i in s:
  rev=i+rev
print(rev)

#Shortcut method

s=input("Enter a string:")
print(s[::-1])