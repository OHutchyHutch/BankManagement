import user
class bankusers:
  def __init__ (self, usersArray):
    self.usersArray = usersArray
  def accessUsers(self):
    return self.usersArray
  def addUsers(self, username, password, deposit):
    self.usersArray.append(user.user(str(username), int(password), int(deposit)))