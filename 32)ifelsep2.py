#decide if an input number is postive even, negative even, positive odd, negative odd ,zero using if else and elif statements
n = int(input("Enter a number:"))
if n > 0:
    if n % 2 == 0:
        print(n, "is a positive even number.")
    else:    
        print(n, "is a positive odd number.")
elif n < 0:
    if n%2 == 0:
        print(n, "is a negative even number.")
    else: 
        print(n, "is a negative odd number.")
else:
    print("The number is zero.")
