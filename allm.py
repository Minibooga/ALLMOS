import hashlib

def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()
  
def login():
  global usrname
  global cfp_hash
  usrname=input("Please input your username: ")
  pwd=input("Please input your password: ")
  cfp=input("Reenter your password: ")
  if cfp==pwd:
    print("Thank you.")
    cfp_hash=hash_password(cfp)
    lockscreen()
  else:
    print("PASSWORDS DO NOT MATCH")
    login()

def lockscreen():
  print("Welcome to ALLM OS")
  un=input("Enter your username: ")
  pw=input(f"Enter {un}'s password: ")
  if un==usrname and pw==cfp:
    print("Welcome to ALLM OS!")
    allmos()
  else:
    print("Invalid username or password.")
    print("Rerun the script, python allm.py")
    print("Program end.")
    




login()
