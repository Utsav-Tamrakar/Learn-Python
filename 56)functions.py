#Functions in Python example
def printDate(d,m,y):
  print(d,m,y,sep="-")

print("Nepal became independent on ")
printDate("04","07","2004")

#getData
def getDate(d,m,y):
  return d+"-"+m+"-"+y

print("Nepal became independent on ")
d= getDate("04","07","2004")
print(d)


#Example
def greet():
  print("HI")
  print("Welcome to GeeksforGeeks")
  
def exit():
  print("Please visit again")
  print("byee")
  
greet()
print("Hope you are enjoying")
exit()


#applications of functions
#Avoid Redundancy and Ease Maintainance
#Make code modular(takeInput(),processData(),produceOutput())
#Abstraction: not need to worry about internal architecture of a functions for example
#Avoid name collisions