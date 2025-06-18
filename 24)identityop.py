#Identity comparision operator ie: is and is not
x=10
y=x
print(x is y)
print(x is not y)

#if both variables have same value then they are allocated at same memory location in python
x=10
y=10
print(x is y) #True
#Examples of Container 
l1=[10,20,30]
l2=[10,20,30]
print(l1 is l2) #False, because they are different objects in memory
