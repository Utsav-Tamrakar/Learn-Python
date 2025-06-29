#Variable Length Arguments : *(star symbol) used for variable length arguments...and is a tuple so can contain multiple number 

def sum(*elements):
  res = 0
  for x in elements:
    res=res + x
  return res

print(sum(10,20))
print(sum(10,20,30))
print(sum(10))
print(sum())

#To print it as id ,name and a price we simply use variable length arguments which take input as a tuple and placed it into a small bracket
def printElements(*elements):
  print(elements)
  
printElements(101,"abc",100)
printElements(102,"xyz",200)