#a and b have same value so there location are same...but c have different value so have different address....
a=10
b=10
print(a is b)
c=a
print(c is b)
c=20
print(c is b)
 
 
 
#booleran represents one of two values: True or False
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#Evaluate a string and a number
print(bool("Hello"))
print(bool(15))

#Evaluate two variables:
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#Most values are True except empty strings  , 0
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
