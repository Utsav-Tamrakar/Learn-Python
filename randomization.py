#used for games for random numbers in case
#this below random.random gives randomized number can be anything 
import random
#print(random.random())

#the below random numbers,we can give the beginning and ending value and then the picked value is then only within the range eg...
#print(random.randint(1,10))

#random value from a list
names = ["ram","shyam","hari","sita"]
random.shuffle(names)
print(names[0])