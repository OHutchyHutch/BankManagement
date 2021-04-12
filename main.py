#DUE APRIL 26th

'''
Things we could do:
- Implement a feature to check Balance
- Implement a case where the user says there is already an account (and initialize some dummy accounts with it)
'''
import user,login, bankusers
bankUsersClass = bankusers.bankusers([])
login = login.login(bankUsersClass)

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