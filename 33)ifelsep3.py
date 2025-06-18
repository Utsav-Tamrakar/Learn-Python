#take a two number from a user and find which one is greater or equal
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
if n1 > n2:
    print(n1, "is greater than", n2)
elif n1 < n2:
    print(n1, "is less than", n2)
else:
    print(n1, "is equal to", n2)