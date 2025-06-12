#list store multiple of items..it is like an array of items and we can access values like an array with extra thing is negative value in an index to display from backside...We can even insert and append in a list...
# List is an ordered, changeable
#l = [10,20,30,40,50]
#print(l)
#print(l[3])
#print(l[-1])
#print(l[-3])

l=[10,20,30,40,50]
l.append(30)
print(l)
l.insert(1,15)
print(l)
print(l.index(30,4,7))
print(15 in l)
print(l.count(30))
print(l.index(30))
print(l)
l.remove(15)
print(l)
print(l.pop(1))
print(l)
del l[2]
print(l)
del l[0:2]
print(l)
print(l.pop())

l=[10,20,30,40,50,60]
print(l)
print(max(l))
print(min(l))
print(sum(l))
l.reverse()
print(l)
l.sort()
print(l)
#if there is string in list and others are number then max,min,sum,reverse,sort functions donot work in it

 