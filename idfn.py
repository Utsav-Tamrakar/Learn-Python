#id function returns the identity of an object
#This is an integer which is guaranteed to be unique and constant for this object during its lifetime
#it is used to check if two variables point to the same object in memory
x = 42
y = x
z = 42

print(id(x))  
print(id(y))  # (same as x)
print(id(z))  # (same as x and y)
if(id(x) == id(y)==id(z)):
    print("x , y & z reference the same object")