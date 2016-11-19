from app.TDG import RoomTDG
from app.core.room import Room
import RoomIdMap
import UnitOfWork

def makeNew(roomId, lock):
    room = Room(roomId, lock)
    RoomIdMap.addTo(room)
    UnitOfWork.registerNewRoom(room)
    return room

def find(roomId):
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

def setRoom(roomId):
    room = find(roomId)
    room.setId(roomId)
    UnitOfWork.registerDirty(roomId)

def delete(roomId):
    room = RoomIdMap.find(roomId)
    if room is not None:
        RoomIdMap.removeFrom(room)
    UnitOfWork.registerDeleted(room)
#save all work
def done():
    UnitOfWork.commit()
#adds room object
def save(room):
    RoomTDG.insert(room)
#updates room Object
def update(room):
    RoomTDG.update(room)
#deletes room object
def erase(room):
    RoomTDG.delete(room)