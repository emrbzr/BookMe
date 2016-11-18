from app.TDG import TimeslotTDG
from app.core.timeslot import Timeslot

import UnitOfWork
import TimeslotIdMap




def makeNew(st, et, date, id):
    timeslot = Timeslot(st, et, date, id)
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
            timeslot = Timeslot(result[0][1], result[0][2], result[0][3], result[0][0])
            TimeslotIdMap.add(timeslot)
   
    return timeslot

def set(timeslotId):
    timeslot = TimeslotMapper.find(timeslot)
    UnitOfWork.registerDirty(timeslot)

#remove timeslot instance from unit of work
def delete(timeslot):
    timeslotId = timeslot.getId()
    timeslot = TimeslotIdMap.find(timeslotId)
    if timeslot is not None:
        TimeslotIdMap.delete(timeslot)
    UnitOfWork.registerDeleted(timeslot)

def save(timeslot):
    WaitingTDG.insert(timeslot)

#remove waiting instance from database
def erase(timeslot):
    timeslotId = timeslot.getId()
    TimeslotTDG.delete(timeslotId)
