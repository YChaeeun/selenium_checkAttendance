class Site :
    def __init__(self):
        self.__url = "http://~~~~.com"
        self.__id_id = "usr_id"
        self.__id_password = "usr_pwd"
        self.__xpath_login = '//*[@id="login_btn"]'

        self.__title = ""
        self.__content = ""

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

    @property
    def title(self) :
        return self.__title

    @property
    def content(self) :
        return self.__content

    @title.setter
    def title(self, date) :
        self.__title = f"<출석 체크> {date}"