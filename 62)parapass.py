#parameter passing in python
def fun(x): #local variable x
  x=15

x=10 #global variable
fun(x)
print(x)

def fun(l):
  l.append(15)
  
l=[10,20,30]
fun(l)
print(l)

#another example
def fun(l):
  l=[40,50]
l=[10,20,30]
fun(l)
print(l)