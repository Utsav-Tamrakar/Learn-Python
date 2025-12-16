#Type-1: Creating a tuple
fruits=('Apple','Orange','Mango')
#type of fruits
print(type(fruits))
#accessing elements
#tuple is unchangeable
print(fruits[0])
print(fruits[1])
print(fruits[2])
#Slicing of tuple
t = (10,20,"geeks")
print(t)
t=(10)
print(type(t))
t=(10,)
print(type(t))

t=(10,20,30,40,10)
print(t[2])
print(t[-1])
print(t[1:3])
print(t.count(10))
print(t.index(20))

#tuple unpacking
tuple=("Geeks","For","Geeks")
a,b,c=tuple
print(a)  
print(b)
print(c)

#Nested Tuple
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3= (tup1, tup2)
print(tup3)

#Concatenation of tuples
tup=tuple+tup1
print(tup)

#Tuple with repetition
tup1 = ('geek',) * 3
print(tup1)

# Tuple with the use of loop
tup=("geeks")
n=5
for i in range(int(n)):
  print(tup)

#we can delete tuple using del keyword
tup=("geeks","for","geeks") 
del tup
#print(tup) #this will raise an error because the tuple has been deleted

#tuple unpacking with asterisk
tup=(1,2,3,4,5,6,7,8,9)
a,b,*c=tup
print(a)
print(b)
print(c)