# User object
class User:

    # Constructor
    def  __init__(self):
        pass
    def __init__(self,userId, name,password):
        self.name = name
        self.password = password

    # Accessors and Mutators
    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password
