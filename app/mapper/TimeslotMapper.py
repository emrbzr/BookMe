from app.TDG import TimeslotTDG
from app.core.timeslot import Timeslot
import UnitOfWork
import TimeslotIdMap
from app.TDG import TimeslotTDG

def makeNew(st, et, date,userId):
    timeslot = Timeslot(st, et, date, userId)
    TimeslotIdMap.add(timeslot)
    UnitOfWork.registerNew(timeslot)
    return timeslot


def find(timeslotId):
    timeslot = TimeslotIdMap.get(timeslotId)
    if timeslot == None:
        result = TimeslotTDG.find(timeslotId)
        if result == None:
            return
        else:
            timeslot = Timeslot(result[0][1], result[0][2], result[0][3], result[0][5])
            TimeslotIdMap.add(timeslot)

    return timeslot

def findId(userId):
    result = TimeslotTDG.find(userId)
    return result[-1][0]


def set(timeslotId):
    timeslot = find(timeslotId)
    UnitOfWork.registerDirty(timeslot)

def done():
    UnitOfWork.commit()

# remove timeslot instance from unit of work
def delete(timeslot):
    timeslotId = timeslot.getId()
    timeslot = TimeslotIdMap.find(timeslotId)
    if timeslot is not None:
        TimeslotIdMap.delete(timeslot)
    UnitOfWork.registerDeleted(timeslot)


def save(timeslot):
    TimeslotTDG.insert(timeslot)


# remove waiting instance from database
def erase(timeslot):
    timeslotId = timeslot.getId()
    TimeslotTDG.delete(timeslotId)