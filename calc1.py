print("*****CALCULATOR*****")
print("\n")
num1=float(input("Enter first number"))
num2=float(input("Enter second number"))

print("Enter 1 for 'Addition' \n Enter 2 for 'Subtraction' \n Enter 3 for 'multiplication'\n Enter 4 for 'Division' ")
Entered_number=int(input("Choice a number from 1 to 4:"))
if Entered_number ==1:
  print("Addition of your first and second number is:",num1+num2)
  
elif Entered_number==2:
  print("Subtraction of your first and second number is:",num1-num2)
elif Entered_number==3:
  print("Multiplication of your first and second number is:",num1*num2)
elif Entered_number:
  print("Division of your first and second number is:",num1/num2)