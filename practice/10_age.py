# Check voting eligibility based on age
n=int(input("Enter your age: "))
if n<18:
  print("you are not eligible to vote")
elif n>=18:
  print("you are eligible to vote")
else:
  print("invalid input")
