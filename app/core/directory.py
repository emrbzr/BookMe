# Directory Object
class Directory:

    # Constructor
    def __init__(self,roomlist):
        self.roomList = roomlist

    # Method to get room based on the Id
    def getRoom(self,roomId):
        for index in range(len(self.roomList)):
            if self.roomList[index].getId() == roomId:
                return self.roomList[index]

    # Accessors and Mutators
    def getRoomList(self):
        return self.roomList

    def setRoomList(self,roomList):
        self.roomList = roomList