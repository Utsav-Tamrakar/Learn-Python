#Find the largest among three numbers
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))  
n3=int(input("Enter third number: "))
# if n1 > n2 and n1 > n3:
#   print(n1, "is the largest number")
# elif n2 > n1 and n2 > n3:
#   print(n2, "is the largest number")
# else:
#   print(n3, "is the largest number")
print(max(n1, n2, n3), "is the largest number")  # Using max function to find the largest number