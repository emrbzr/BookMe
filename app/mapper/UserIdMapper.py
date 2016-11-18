userList = []
#constructor
def __init__(self):
	pass

#add user to list
def addTo(self, user):
	self.userList.append(self.user)

#remove user from list
def removeFrom(self, user):
	self.userList.remove(self.user)

#find user from list
def find(self, userId):
	for i in range(len(self.userList)):
		if self.userId in self.userList:
			return self.userList[i]
	return
