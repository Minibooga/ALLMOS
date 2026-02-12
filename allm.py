import hashlib
import os
import json


USERS_FILE = "users.json"

def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()

def load_users():
  """Load users from file"""
  if os.path.exists(USERS_FILE):
    try:
      with open(USERS_FILE, "r") as f:
        return json.load(f)
    except Exeption:
        return {}
    return  {}

def save_users(users):
  """Save users to file"""
  with open(USERS_FILE, "w") as f:
    json.dump(users, f, indent=4)


  
def login():
  global usrname
  global cfp_hash
  users=load_users()

  while True:
    print("\n---LOGIN---")
    print("1. Login")
    print("2. Register")
    option=input("Select:")

    if option=="1":
      usrname = input("Enter your username: ")
      pwd = input("Enter your password: ")

      if usrname in users and hash_password(pwd) == users[usrname]:
        cfp_hash=users[usrname]
        print("Login succsessful.")
        allmos()
        break
      else:
        print("Invalid username or password. Did you have an account saved?")

    elif choice == "2":
      usrname=input("Please input your username: ")
    if usrname in users:
      print("User exists.")
      continue

    pwd=input("Please input your password: ")
    cfp=input("Reenter the password: ")
    
    if pwd==cfp:
      cfp_hash = hash_password(pwd)
      users[usrname] = cfp_hash
      save_users(users)
      print("Thank you.")
      lockscreen()
      break
  else:
    print("PASSWORDS DO NOT MATCH")

def lockscreen():
  global cfp_hash
  global usrname
  print("Welcome to ALLM OS")

  while True:
    un=input("Enter your username: ")
    pw=input(f"Enter {un}'s password: ")
    if un==usrname and hash_password(pw)==cfp_hash:
      print("Welcome to ALLM OS!")
      allmos()
      break
    else:
      print("Invalid username or password.")

def allmos():
  print("welcome to ALLM OS 1.")
  while True:
    print("\n--Utility Launcher--")
    print("1. Files")
    print("2. Notes")
    print("3. Passwords")
    print("4. Bye-bye!")
    option = input("Select program: ")

    if option == "1":
      file_manager()
    elif option == "2":
      note_app()
    elif option == "3":
      password_manager()
    elif option == "4":
      print("logging out...")
      break
    else:
      print("Not an option.")
    




login()
