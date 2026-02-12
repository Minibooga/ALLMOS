import hashlib

def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()
  
def login():
  global usrname
  global cfp_hash
  usrname=input("Please input your username: ")
  pwd=input("Please input a password that will be hashed: ")
  cfp=input("Reenter the password: ")
  if cfp==pwd:
    print("Thank you.")
    cfp_hash=hash_password(cfp)
    print("Your password is:", cfp_hash)
    lockscreen()
  else:
    print("PASSWORDS DO NOT MATCH")
    login()

def lockscreen():
  global cfp_hash
  global usrname
  print("Welcome to ALLM OS")
  un=input("Enter your username: ")
  pw=input(f"Enter {un}'s password: ")
  if un==usrname and pw==cfp_hash:
    print("Welcome to ALLM OS!")
    allmos()
  else:
    print("Invalid username or password.")
    lockscreen()
    




login()
