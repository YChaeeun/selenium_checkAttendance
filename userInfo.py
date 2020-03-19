class User :
    def __init__(self):
        self.__id = "201X0000"
        self.__password = "123456789"

    @property
    def id(self):
        return self.__id

    @property
    def password(self):
        return self.__password

    @id.setter
    def id(self, userId):
        self.__id = userId
    
    @password.setter
    def password(self, userPwd) :
        self.__password = userPwd
