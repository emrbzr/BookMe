import UserMapper

newList = []
changedList = []
deletedList = []
def __int__(self):
	pass

def registerNew(self,user):
    newList.append(user)

def registerDirty(self, user):
	changedList.append(user)

def registerDeleted(self, user):
	deletedList.add(user)

def commit(self):
    UserMapper.addUser(newList)
    UserMapper.updateUser(changedList)
    UserMapper.deleteUser(deletedList)
    del newList[:]
    del changedList[:]
    del deletedList[:]