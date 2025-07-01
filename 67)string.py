#String is a sequence of characters,used to store text data,like data read from a file...
#typically small set of characters,characters 'A' to 'Z' are stored as values from 65 to 90,characters 'a' to 'z' are stored as values from 97 to 122
#First program of string
print(ord('a')) 
print(ord('A')) 
print(chr(97))  
print(chr(65))  
#Second program of string
x='geek'
print(x)
print(x[0])
print(x[-1])
print(x[1])
print(x[-3])

#3rd program to demonstrate Strings are immutable in python like as in a java
# s="geek"
# s[0]="e"
# print(s)
#its output:TypeError: 'str' object does not support item assignment

#4th program
s="""Hi,
My name is Utsav Tamrakar
And I'm learning "Python" language.."""
print(s)