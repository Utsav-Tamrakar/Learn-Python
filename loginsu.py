atm_user_id = 10
atm_user_pin =0000

inputid= int(input("Enter user id: "))
inputpin= int(input("Enter pin: "))

if atm_user_id == inputid and atm_user_pin == inputpin :
  print("Login successful")
else:
  print("Login failed")
  
   