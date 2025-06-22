#LCM:Least Common Multiple 
import math
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
# res = max(a,b)
# while(res<=a*b):
#   if(res%a==0 and res%b==0):
#     break
#   res +=1
# print("LCM is ",res)
#Another approach
# gcd = math.gcd(a,b) 
# lcm = (a*b)/gcd
lcm=math.lcm(a,b)
print("LCM of a and b: ",lcm)