#Implicit Type conversion
a=10
b=1.5
c=a+b
print(c)
d=True
e=a+d
print(e)

#Explicit type conversion
#program 1
s="135"
i=10+int(s)
f=float(s)
print(i)
print(f) 

#program 2
s="geeks"
print(list(s))
print(tuple(s))
print(set(s))

#program 3
l=['a','b','c']
print(str(l))
a=10
b=11
print(str(a)+str(b)) #concatenation of a and b
c=12.5
print(str(c))

#program 4
t=(10,20,30)
print(list(t))
s={10,20,30}
print(list(s))

#program5
a=20
print(bin(a))
print(hex(a))
print(oct(a))

#program6
a="1001"
print(int(a,2)) #tells binary
b="12"
print(int(b,8)) # tells octal
c="A1"
print(int(c,16)) #tells hexadecimal
