# User object
class User:

    # Constructor
    def __init__(self,name:str,email:str,password:str):
        self.name = name
        self.userId = id(self)
        self.email = email
        self.password = password

    # Accessors and Mutators
    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getUserId(self):
        return self.userId

    def setUserId(self,userId:int):
        self.userId = userId

    def getEmail(self):
        return self.email

    def setEmail(self,email:str):
        self.email = email

    def getPassword(self):
        return self.password

    def setPassword(self, password:str):
        self.password = password
