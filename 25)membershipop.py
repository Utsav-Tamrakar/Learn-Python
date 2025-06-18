#string:Checks for substring membership in a string
s="Utsav tamrakar"
print("s" in s)
print("sav" in s)  # True, 'sav' is a substring of 'Utsav tamrakar'

#dictionary:Checks for key membership in a dictionary
d={10:"Utsav",20:"Tamrakar"}
print(10 in d)  # True, 10 is a key in the dictionary
print(15 in d)  # False, 15 is not a key in the dictionary
print("Utsav" in d)  # False, 'Utsav' is not a key in the dictionary

#list,set,tuple:Checks for element membership in a list, set, or tuple
l=[10, 20, 30]
print(10 in l)  # True, 10 is an element in the list
print([20,30] in l)  # False, [20, 30] is not an element in the list

s={10, 20, 30}
print(10 in s)  # True, 10 is an element in the set