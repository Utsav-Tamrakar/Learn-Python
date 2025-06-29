#positional and keyword argument in detail
#creating a function
def printItem(id,name,price):
  print(f"Id is {id}")
  print(f"Name is {name}")
  print(f"Price is {price}")
#main program
#Postional argument if fixed according to the function
printItem(101,"abc",100)
print()
#keyword arguments we can switch any position but need to include their variable names defines in a function
printItem(id=105,name="xyz",price=200)
print()

printItem(price=500,id=200,name="xzz")
print()