# Set is unordered,unchangeable and unindexed 
myList = {'Python','Java','C++'}
print(type(myList))
print(myList)   

s1 = {10,20,30}
print(s1)
s2=set([20,30,40]) # here set constructor is used 
print(s2)
s3 = { } #empty set but it shows its type as dictionary
print(type(s3))
s4 = set()
print(type(s4))
print(s4)

s = {10,20}
print(s)
s.add(30)
print(s)
s.update([40,50])
print(s)
s.update([60,70],[80,90])
print(s)

t={10,20,30,40}
print(10 in t)
print(50 in t)
t.discard(30) #if the value is not present in a set then is neglectedd
print(t)
t.remove(20)#if the value is not present then it shows an error 
print(t)
t.clear()
print(t)
t.add(50)
print(t)
print(len(t))
del t 

s1={2,4,6,8}
s2={3,6,9}
print(s1|s2) #s1.union(s2)
print(s1&s2) #gives intersection also s1.intersection(s2)
print(s1-s2) #present in s1 not in s2 also s1.difference(s2)
print(s1^s2) #gives symmetric difference also by s1.symmertric_difference(s2)

s1={2,4,6,8}
s2={4,8}
print(s1.isdisjoint(s2))
print(s1 <= s2)
print(s1<s2)
print(s1 >= s2)
print(s1 > s2)