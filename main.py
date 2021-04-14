#DUE APRIL 26th

'''
Things we could do:
- 
'''
import user,login, bankusers
bankUsersClass = bankusers.bankusers([])
bankUsersClass.addUsers("John", 123, 50)
bankUsersClass.addUsers("Sally", 321, 0)
login = login.login(bankUsersClass)

isLoggedIn, accessedUser = login.isRegistered()

while(isLoggedIn):
  print("\n\n---------------")
  print("Current Balance: $" + str(accessedUser.getMoney()))
  print("---------------")
  print("\n1. Deposit\n2. Withdraw\n3. Logout")
  action = str(input("\n\nWhat would you like to do:  "))
  if (action == "Logout" or action == "3"):
    print("Goodbye, " + accessedUser.getName())
    isLoggedIn = False
    break
  amount = int(input ("How much? "))
  if (action == "Deposit" or action == "1"):
    accessedUser.addMoney(amount)
  elif (action == "Withdraw" or action == "2"):
    accessedUser.removeMoney(amount)