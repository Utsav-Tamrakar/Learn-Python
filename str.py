#string is surrounded by either single quotation mark or double quotation mark
#'hello' or "hello"
a="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua"""
print(a)


#interms of array
a="Hello,World"
print(a[3])


#loop through a string
for x in "banana":
  print(x)


#for a string length
b="Utsav Tamrakar"
print(len(b))


#check string
txt="The best things in life are free"
print("free" in txt)
  
  #also we can do like
txt="The best things in life are free"
if "free" in txt:
  print("Yes,'free' is present")


#check if not bool
txt="The best things in life are free"
print("expensive" not in txt)


#slicing:specify the start and end index separated by a colon,to return a part of a string
c='Utsav'
print(c[2:5])
#slice from start
print(c[:5])

#slice to the end
print(c[1:])

#negative indexing
print(c[-5:-1])


#uppercase and lowercase
a="Utsav Tamrakar"
print(a.upper())
print(a.lower())

#remove whitespace
print(a.strip())

#replace a string
print(a.replace("T" ,"t"))

#split string
print(a.split(","))

#concatenation string
a="Hello"
b="World"
c=a+b
print(c)
c=a+" "+b
print(c)
