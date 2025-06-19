#python program to print a table of a number
import sys
print("Please enter a number to print its table : ")
n = int(input("Enter a number:"))
if int(n) < 0:
  print("Negative number entered")
  sys.exit("Exiting the program")
print("Table of", n)
for i in range (1,11):
  print(n, "x", i, "=" ,n*i)
print("Thank  you for using this table program")