from app.TDG import WaitingTDG
from app.core.waiting import Waiting
import UnitOfWork
import WaitingIdMap
import RoomMapper
import UserMapper
import TimeslotMapper


def makeNew(room, description, reservee, timeslot):
    waiting = Waiting(room, reservee, timeslot, description)
    WaitingIdMap.add(waiting)
    UnitOfWork.registerNew(waiting)
    return waiting


def find(waitingId):
    waiting = WaitingIdMap.get(waitingId)
    if waiting == None:
        result = WaitingTDG.find(waitingId)
        if result == None:
            return
        else:
            room = RoomMapper.find(result[0][1])
            reservee = UserMapper.find(result[0][2])
            timeslot = TimeslotMapper.find(result[0][4])
            waiting = Waiting(room, result[0][3], reservee, timeslot)
            WaitingIdMap.add(waiting)

    return waiting


def set(waitingId):
    waiting = find(waitingId)
    UnitOfWork.registerDirty(waiting)

def done():
    UnitOfWork.commit()

# remove waiting instance from unit of work
def delete(waiting):
    waitingId = waiting.getId()
    waiting = WaitingIdMap.find(waitingId)
    if waiting is not None:
        WaitingIdMap.delete(waiting)
    UnitOfWork.registerDeleted(waiting)


def save(waiting):
    WaitingTDG.insert(waiting)

def update(waiting):
    WaitingTDG.update(waiting)
# remove waiting instance from database
def erase(waiting):
    waitingId = waiting.getId()
    WaitingTDG.delete(waitingId)