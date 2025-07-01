#Formatted string in python 
#1)Using C approach in a python
name="ABC"
course="Python Course"
s="Welcome %s to the %s"%(name,course)
print(s)
#2)Using format() function
name="ABC"
course="Python Course"
s="Welcome {0} to the {1}".format(name,course)
print(s)

#3)Using f-string
name="ABC"
course="Python Course"
s=f"Welcome {name} to the {course}"
print(s)