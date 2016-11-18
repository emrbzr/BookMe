from app.TDG import UserTDG
from app.core.user import User

import UnitOfWork
import UserIdMapper


def __init__():
    pass


def makeNew(name, password):
    user = User(name, password)
    UserIdMapper.addTo(user)
    UnitOfWork.registerNew(user)
    return user


def getUser(self, userId):
    user = UserIdMapper.find(userId)
    result = []
    if user == None:
        result = UserTDG.find(userId)
    if result == None:
        return
    else:
        user = User(result[0], result[1], result[1])
        UserIdMapper.addTo(user)
        return user

def setUser(self, userId):
    user = getUser(userId)
    user.setName(self.getName())
    UnitOfWork.registerDirty(user)


def delete(self, userId):
    user = UserIdMapper.find(userId)
    if user is not None:
        UserIdMapper.removeFrom(user)
    UnitOfWork.registerDeleted(user)

def done():
    UnitOfWork.commit()

def addUser(user):
    UserTDG.insert(user)

def updateUser(user):
    UserTDG.update(user)

def deleteUser(userId):
    UserTDG.delete(userId)
