reservationList = []
#constructor
def __init__(self):
	pass

#add user to list
def addTo(self, reservation):
    reservationList.append(reservation)

#remove user from list
def removeFrom(self, reservation):
    reservationList.remove(reservation)

#find user from list
def find(self, reservationId):
	for i in range(len(reservationList)):
		if reservationId in reservationList:
			return reservationList[i]
	return
