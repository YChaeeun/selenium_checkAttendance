class Site :
    def __init__(self):
        self.__url = "http://~~~~.com"
        self.__id_id = "usr_id"
        self.__id_password = "usr_pwd"
        self.__xpath_login = '//*[@id="login_btn"]'

    @property
    def url(self) :
        return self.__url
    
    @property
    def put_id(self) :
        return self.__id_id

    @property
    def put_password(self) :
        return self.__id_password
        
    @property
    def btnLogin(self) :
        return self.__xpath_login