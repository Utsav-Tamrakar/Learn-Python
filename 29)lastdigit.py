#find out last digit of a number
#Only runs when value of x is greater or equal to 0
x=int(input("Enter a number: "))
ld=x%10  # Last digit is the remainder when divided by 10
print("The last digit of", x, "is:", ld)

#for any value of x, we can find the last digit
ld=abs(x%10)
print("The last digit of", x, "is:", ld)