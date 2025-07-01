#Escape sequences and Raw strings
#Example of Escape sequences
# s='Welcome to Geek's Course' 
# print(s)
#this program shows output invalid 
#Corrected program is using escape sequence i.e \
s='Welcome to Geeks\'s Course'
print(s)

#Another example,\n is used to escape a new line 
s="Hi, \n Welcome to the course"
print(s)

#escaping the backslash itself
s1="A simple \ example"
s2="Backslash at the end \\"
s3="\\n"
s4="\\t"
print(s1)
print(s2)
print(s3)
print(s4)

#Example of Raw strings :
s1="c:\project\name.py"
s2=r"c:\project\name.py" #we can see the use of r and the outputs
print(s1)
print(s2)