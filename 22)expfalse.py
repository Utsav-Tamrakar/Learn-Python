#Expressions that are treated as false: None,Empty string,list,tuple,dictionary etc
s1=""
s2=s1 or "default"
print(s2)
s1="hey"
s2=s1 or "default"
print(s2)

#if there is non zero on a variable then it will print the nonzero value if the value is zero or empty it will print another value shown using or operator
x=10
print(x or 20)
y=0
print(y or 30)
z=50 
print(z or 20)