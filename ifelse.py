# if else concept with driving age
age = 17
 
if age>=18:
    print("You are eligible to drive")
else:
    print("You are not eligible to drive")  

# the condition must be true and even numbers and strings can work
#if false the doesn't execute the block
if True:
    print("HEllO")

#elif use show with taxi,bike and car
vehicle="car"
if vehicle == "bike":
    print("Rs 100 per day")
elif vehicle == "car":
    print("Rs 500 per day") 
elif vehicle == "taxi":
    print("Rs 1000 per day")
else:
    print("Invalid vehicle")    
