from app.TDG import RoomTDG
from app.core.room import Room
import RoomIdMap
import UnitOfWork

def makeNew(self,roomId, lock):
    room = Room(roomId, lock)
    RoomIdMap.addTo(room)
    UnitOfWork.registerNewRoom(room)
    return room

def getRoom(self, roomId):
    room = RoomIdMap.find(roomId)
    result = []
    if room == None:
        result = RoomTDG.find(roomId)
    if result == None:
        return
    else:
        room = Room(result[0], result[1])
        RoomIdMap.addTo(room)
        return room

def setRoom(self, roomId):
    room = getRoom(roomId)
    room.setId(roomId)
    UnitOfWork.registerDirty(roomId)

def deleteRoom(self, roomId):
    room = RoomIdMap.find(roomId)
    if room is not None:
        RoomIdMap.removeFrom(room)
    UnitOfWork.registerDeleted(room)
#save all work
def save():
    UnitOfWork.commit()
#adds room object
def addRoom(room):
    RoomTDG.insert(room)
#updates room Object
def updateRoom(room):
    RoomTDG.update(room)
#deletes room object
def deleteRoom(room):
    RoomTDG.delete(room)