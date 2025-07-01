#Program checks for substring
s1="geeksforgeek"
s2="geeks"
print(s2 in s1)
print(s2 not in s1)
#Concatenation of substrings
s1="geeks" 
s2="forgeeks" 
s3=s1+s2
s4="Welcome to "+ s1 + s2
print(s3)
print(s4)
#To find position of a substring
s1="geeksforgeeks"
s2="geeks"
print(s1.index(s2))    #shows index from first so i.e. 0
print(s1.rindex(s2))   #shows index from last so i.e. 8
print(s1.index(s2,0,13))   
print(s1.index(s2,1,13))   #starting and ending index of a given string 