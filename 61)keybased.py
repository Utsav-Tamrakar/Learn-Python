#we initialize for keyword based variable length arguments using ** in an argument
def printDetails(**details):
  for d,v in details.items():
    print(f"{d} is {v}")

printDetails(id=100,name="ram",price=1000)
print()
printDetails(id=101,name="shyam",price=2000)
print()
#another example additional parameter ID
def printDetails(id,**details):
  print(f"Details of {id}: ")
  for d,v in details.items():
    print(f"{d} is {v}")

printDetails(100,name="ram",price=1000)
print()
printDetails(101,name="shyam",color="black")
print()