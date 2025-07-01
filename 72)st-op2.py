#String operator
#Example-1
s1="geeks"
print(len(s1))
s2=s1.upper()
print(s2)
s3=s2.lower()
print(s3)
print(s1.islower())
print(s2.isupper())
#Example-2 starts with and end with methods
s="GeeksforGeeks Python Course"
print(s.startswith("Geeks"))
print(s.endswith("Course"))
print(s.startswith("Geeks,1"))
print(s.startswith("Geeks",8,len(s)))  

#Example-3:split and join method in python
s1="geeks for geeks"
print(s1.split())
s2="geeks,for,geeks"
print(s2.split(","))
l=["geeksforgeeks","python","course"]
print(" ".join(l))
print(",".join(l))
#Example-4:strip which removes unwanted characters from corners of string
s="--geeksforgeeks---"
print(s.strip("-"))
print(s.lstrip("-"))
print(s.rstrip("-"))

#Example-5 : find() method 
s1="geeks for geeks"
s2="geeks"
print(s1.find(s2))
print(s1.find("gfg"))
n=len(s1)
print(s1.find(s2,1,n))
