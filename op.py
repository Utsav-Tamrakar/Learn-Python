atm_user_id = 10
atm_user_pin = 5555

inputid = int(input("Enter user id : "))
inputpin = int(input("Enter pin : "))

if atm_user_id == inputid and atm_user_pin == inputpin :
  print("Login Successful")
else:
  print("Login Failed")
  
  