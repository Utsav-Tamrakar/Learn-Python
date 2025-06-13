fruits=('Apple','Orange','Mango')

print(type(fruits))
print(fruits[0]) #tuple is unchangeable

t = (10,20,"geeks")
print(t)
print(type(t))
print(t)
t=(10)
print(type(t))
t=(10,)
print(type(t))

t=10,20,30,40,10
print(t[2])
print(t[-1])
print(t[1:3])
print(t.count(10))
print(t.index(20))