#DUE APRIL 26th


import user,login, bankusers
bankUsersClass = bankusers.bankusers([])
login = login.login(bankUsersClass)

isLoggedIn = False
accessedUser = user.user("",0,0)

isLoggedIn, accessedUser = login.isRegistered()
while(isLoggedIn):
  action = str(input("\n\nWhat would you like to do? Deposit/Withdraw/Logout: "))
  if (action == "Logout"):
    print("Goodbye, " + accessedUser.getName())
    isLoggedIn = False
    break
  amount = int(input ("How much? "))
  if (action == "Deposit"):
    accessedUser.addMoney(amount)
  elif (action == "Withdraw"):
    accessedUser.removeMoney(amount)
    
  print("Current Balance: " + str(accessedUser.getMoney()))