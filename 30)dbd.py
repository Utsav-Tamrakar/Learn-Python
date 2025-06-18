#day before n days
d=int(input("Enter the number of days: "))
n=int(input("Enter the number of days before today: "))
print((d - n) % 7)  # Calculate the day of the week n days before d