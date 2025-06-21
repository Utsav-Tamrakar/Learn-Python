#triangular patterns
n=int(input("Enter a number:"))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
    
#inverted triangular patterns
n=int(input("Enter a number:"))
# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()
for i in range(n):
  for j in range(n-i):
    print("*", end=" ")
  print()