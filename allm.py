def login():
  global usrname
  global cfp
  usrname=input("Please input your username: ")
  pwd=input("Please input your password: ")
  cfp=input("Reenter your password: ")
  if cfp==pwd:
    print("Thank you.")
    lockscreen()
  else:
    print("PASSWORDS DO NOT MATCH")
    login()

def lockscreen():
  print("Welcome to ALLM OS")
  un=input("Enter your username: ")
  pw=input("Enter ", usrname, "'s password: ")
  if pw==cfp:
    print("Welcome to ALLM OS!")
    allmos()
  else:
    print("Invalid username or password.")
    lockscreen()




login()
