print("Utsav Tamrakar")
print("Utsav \n Tamrakar")  #\n new line
print("Utsav \t Tamrakar") #\t tab
# for single or double quotes we use \' and \"
name = "    Utsav tamrakar     "
 
print(name.upper())
print(name.lower())
#print(f"{name.split(" ")[0].capitalize()}{name.split(" ")[1].capitalize()})
print(name.title())
#strip is used to remove spaces and trailing gapes
print(name.strip())
#replacing 
print(name.replace("Utsav","Suman"))
#for lists
names= 'ram , shyam , hari'
lists = names.split(",")


for n in lists:
  print(n)
  