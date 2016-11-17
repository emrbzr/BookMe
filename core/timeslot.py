# Timeslot object
class Timeslot:

    # Constructor
    def __init__(self, startTime:int, endTime:int, date:str, timeId:int):

        self.startTime = startTime
        self.endTime = endTime
        self.date = date
        self.block = endTime - startTime
        self.timeId = timeId

    # Print method for debugging
    def print(self):
        print("Timeslot Info")
        print("StartTime: " + str(self.startTime))
        print("EndTime: " + str(self.endTime))
        print("Date: " + str(self.date))
        print("Duration: " + str(self.block))
        print("TID: " + str(self.timeId))

    # Accessors and Mutators
    def getStartTime(self):
        return self.startTime

    def setStartTime(self,startTime:int):
        self.startTime = startTime

    def getEndTime(self):
        return self.endTime

    def setEndTime(self,endTime:int):
        self.endTime = endTime

    def getDate(self):
        return self.date

    def setDate(self,date:str):
        self.date = date

    def getBlock(self):
        return self.block

    def setBlock(self, block:int):
        self.block = block

    def getId(self):
        return self.timeId

    def setId(self,timeId:int):
        self.timeId = timeId