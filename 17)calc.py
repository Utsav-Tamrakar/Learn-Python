import sys
print("""Please select an operation:
      1) Addition
      2) Subtraction
      3) Multiplication""")
choice=int(input("Select operation from 1-3 : "))
if choice not in (1,2,3):
  print("Invalid choice")
  sys.exit("Exiting the program")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if choice == 1:
  print("Result of addition operation is: ",a+b)
elif choice == 2:
  print("Result of subtraction operation is: ",a-b)
elif choice == 3:
  print("Result of multiplication operation is: ",a*b)
print("Thank you for using the calculator!")