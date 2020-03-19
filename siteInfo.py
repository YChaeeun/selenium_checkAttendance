class Site :
    def __init__(self):
        self.__url = "http://~~~~.com"
        self.__id_id = "usr_id"
        self.__id_password = "usr_pwd"
        self.__xpath_login = '//*[@id="login_btn"]'

        self.__title = "<출석 체크>"
        self.__content = "댓글로 출석체크"

        self.__title_complete = "출결 결과"
        self.__content_complete = "지각 - \n결석 - "

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

    @property
    def title_complete(self) :
        return self.__title_complete

    @property
    def content_complete(self) :
        return self.__content_complete

    @title.setter
    def title(self, date) :
        self.__title = f"<출석 체크> {date}"

    @title_complete.setter
    def title_complete(self, date) :
        self.__title_complete = f"{date} 출결 결과"

    @content_complete.setter
    def content_complete(self, vals) :
        late, absent = vals
        self.__content_complete = f"지각 - {late}\n결석 - {absent}"