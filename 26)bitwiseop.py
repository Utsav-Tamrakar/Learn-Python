# In bitwise operations, we can convert numbers to binary and reverse and perform operations on each bit

print(bin(18))
print(bin(1))
print(int("10010", 2))  # Convert binary string to integer

#bitwise AND
print(3 & 6)  # 2, binary: 011 & 110 = 010

#bitwise OR
print(3 | 6)  # 7, binary: 011 | 110 = 111

#bitwise XOR
print(3 ^ 6)  # 5, binary: 011 ^ 110 = 101

#left shift operation
x=5
print(x << 1)  # 10, binary: 101 << 1 = 1010 (shifts bits to the left)
print(x << 3)  # 10, binary: 101 << 3 = 101000 (shifts bits to the left)

#right shift operation
y=5
print(y >> 1)  # 2, binary: 101 >> 1 = 010 (shifts bits to the right)
print(y >> 3) # 0 , binary:101 >> 3 = 000 (shifts bits to the right)
 
#binary NOT operation\
x=5
print(~x)  # -6, binary: ~101 = ...11111010 (inverts all bits, two's complement representation)