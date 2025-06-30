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

#another example:When the function call is made then the local variable points towards the list of 40,50 whereas 10,20,30 are of global variable
def fun(l):
  l=[40,50]
l=[10,20,30]
fun(l) #function call 
print(l)