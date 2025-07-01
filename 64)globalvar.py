#global variable: Variable which is created outside the function and outside the class is0 called global variable..
#local variable:Variable which is created inside function or class is called local variables...
def fun():
  x=10 #local variable 
x=15 #global variable
fun() #this function will locate a local variable separately and assign x = 10 
print(x) #output will be 15 

#To resolve this we need to clarify in the function to be global only then the output will be assign as we want
def fun():
  global x
  x=10
x=15
fun()
print(x)

#another example
def fun():
  y=x+5
  print(y)
x=15
fun()
# #error local variable x referenced before assignment
# def fun():
#   x=x+5
#   print(x)
# x=15
# fun()

def fun():
  x=10
  globals()['x']=20
  print(x)
  
x=15
fun()
print(x)