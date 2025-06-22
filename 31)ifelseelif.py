# if else and elif statements
# checks odd or even number 
n=int(input("Enter a number to check if it is odd or even:"))
if n % 2 == 0:
    print(n, "is an even number.")
else:
    print(n, "is an odd number.")

# checks if number is positive, negative or zero
if n > 0:
    print(n, "is a positive number.")
elif n < 0:
    print(n, "is a negative number.")
else:
    print("The number is zero.")

# checks if number is divisible by 5 or not
