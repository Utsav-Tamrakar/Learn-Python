#Returning multiples values in python
def add_multiply(x,y):
  sum=x+y
  mul=x*y
  return sum,mul

s,m=add_multiply(10,20)
print(s)
print(m)
  

#Program which return three values
def add_mul_sub(x,y):
  sum=x+y
  mul=x*y
  sub=x-y
  return sum,mul,sub
s,m,sb=add_mul_sub(20,10)
print(s)
print(m)
print(sb)

#returning this element as a list
def add_mul_sub(x,y):
  sum=x+y
  mul=x*y
  sub=x-y
  return [sum,mul,sub]

s,m,sb=add_mul_sub(10,20)
print(s)
print(m)
print(sb)