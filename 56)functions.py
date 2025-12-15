#Functions in Python example
def printDate(d,m,y):
  print(d,m,y,sep="-")

print("Nepal became independent on ")
printDate("04","07","2004")

#getDate function which returns date in d-m-y format
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

#Use of parameters in functions-someone increased marks of students
def increase_marks(marks):
  marks=marks+30
  return marks
student1_marks=70
student2_marks=85
student1_marks=increase_marks(student1_marks)
student2_marks=increase_marks(student2_marks) 
print(student1_marks)
print(student2_marks) 


#Challenge 1:Lets say Nepal has traffic fine Rs.1500 and 20% of the money is contributed to road construction.Make  a function that can calculate money for the road construction...

def road_construction_fee(fine):
  contribution = fine * 0.20
  return contribution

fine_amount = 1500
contribution_amount = road_construction_fee(fine_amount)
print(f"Amount contributed to road construction: Rs.{contribution_amount}")




#applications of functions
#Avoid Redundancy and Ease Maintainance
#Make code modular(takeInput(),processData(),produceOutput())
#Abstraction: not need to worry about internal architecture of a functions for example
#Avoid name collisions
