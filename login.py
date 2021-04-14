import bankusers

class login:
  def __init__(self,bankUsersClass):
    self.bankUsersClass = bankUsersClass
  
  def loggingIn(self):
    print("---------------------")
    print("LOGIN FORM")
    print("---------------------")
    loggingIn = True
    while loggingIn:
      accessedUser = None
      name = str(input("Username: "))
      #For each user in the array, check if their username exists.
      for users in self.bankUsersClass.accessUsers():
        #If username is found, ask for password.
        if (users.getName() == name):
          accessedUser = users
          password = input("Password: ")
          #If password is found, user is now logged into the next while loop and can take actions
          if (accessedUser.checkPassword(password)):
            loggingIn = False
            return True, accessedUser
          else:
            print("Password incorrect! Retry \n\n")
        #Username was not found.
        else:
          print("That name does not exist! \n")

  def isRegistered(self):
    answer = input("Do you already have an account with us? Yes/No : ")
    if (answer == "No"):
      print("---------------------")
      print("REGISTER FORM")
      print("---------------------")
      username = input("Username: ")
      password = int(input("Password (Numbers Only): "))
      self.bankUsersClass.addUsers(username, password, 0)
      print("\n\n\nACCOUNT CREATED... Loading login form\n\n\n")
      return(self.loggingIn())
    else:
      return self.loggingIn()