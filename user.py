class user:
  def __init__ (self, name, password, amount):
    self.name = str(name)
    self.password = str(password)
    self.amount = amount
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