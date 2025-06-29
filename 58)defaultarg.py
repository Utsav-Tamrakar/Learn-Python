#default argument in python
def printDetails(id,name="NA",price="NA"):
  print(f"Id is {id}")
  print(f"Name is {name}")
  print(f"Price is {price}")

#main code
printDetails(name="utsav",id=80)
print()
printDetails(price=10000,id=100)
print()
printDetails("id=101")
#default arguments allow you to define functions with parameters that have default values. If the caller doesn't provide a value for such a parameter, the default value is used.
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Uses default greeting
greet("Bob", "Good evening")  # Overrides default

#Default arguments must follow non-default arguments:
def func(a, b=2):  #  Valid
    pass

# def func(a=1, b):  # Invalid: non-default argument follows default
#     pass
