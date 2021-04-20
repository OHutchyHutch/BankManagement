class user:
  def __init__ (self, name, password, amount, credit):
    self.name = str(name)
    self.password = str(password)
    self.amount = amount
    self.credit = credit
  def getName(self):
    return str(self.name)
  def checkPassword(self, password):
    if (password == self.password):
      return True
    else:
      return False
  def getMoney(self):
    return self.amount
  def addMoney(self, amount):
    self.amount += amount
  def removeMoney(self, amount):
    self.amount -= amount
  def getCredit(self):
    return self.credit
  def loanCheck(self):
    if self.credit <= 650:
      print("Sorry, your credit score is too low for a personal loan.")
    elif self.credit > 650:
      print("Congratulation! You're eligible for a personal loan.")
