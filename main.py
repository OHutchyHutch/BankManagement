#DUE APRIL 26th

import user, login, bankusers, messenger
bankUsersClass = bankusers.bankusers([])
bankUsersClass.addUsers("John", 123, 50, 700)
bankUsersClass.addUsers("Sally", 321, 0, 350)
login = login.login(bankUsersClass)
messenger = messenger.messenger()

isLoggedIn, accessedUser = login.isRegistered()

while True:
  while(isLoggedIn):
    messenger.actionForm(accessedUser.getMoney())
    action = int(input("\n\nWhat would you like to do:  "))

    if (action == 1):
      amount = int(input ("Please Enter An Amount: $"))
      accessedUser.addMoney(amount)

    elif (action == 2):
      amount = int(input ("Please Enter An Amount: $"))
      accessedUser.removeMoney(amount)
  
    elif (action == 3):
      messenger.creditForm(accessedUser.getCredit())
      accessedUser.loanCheck()

    elif (action == 4):
      print("Goodbye, " + accessedUser.getName() + "\n\n\n")
      isLoggedIn = False
      break

  isLoggedIn, accessedUser = login.isRegistered()