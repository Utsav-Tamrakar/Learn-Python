num1=10  #integer
num2=5.5 #float
name="Utsav" #string
a=2+4j

#In list ,it is ordered collection of item...  changeable value
names = ['Utsav','Rinki','Sabnam','Sonam']
#tuple:It is also like a list...you cannot modify ,non changeable
tup = (10,20,30)
print(type(tup))
#set:fast operation ,not any ordered,used hashing,not repeated items 
set = {30,20,10}
print(type(set))
#dictionary:to store mapping,collection of key value pair,rollno and name of student 
dict={10:"utsav",20:"proo"}
print(type(dict))
salary=[100.0,2000,3000]

print(type(a))
print(type(num1))
print(type(num2))
print(type(name))
print(type(names))
print(type(salary[0])) 
print(type(salary[1])) 
print(f"{names[0]} salary is {salary[0]}")
print(f"{names[1]} salary is {salary[1]}")
print(f"{names[2]} salary is {salary[2]}")

print(names[1])
print(names[0])
#nonetype
z=None
print(type(z))
