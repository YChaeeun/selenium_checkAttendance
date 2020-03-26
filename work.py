from userInfo import User 
from siteInfo import Site 

from student import student_dict

from selenium import webdriver as wd

from datetime import datetime
import time

driver = wd.Chrome("./tools/chromedriver.exe")  # 제어할 웹 브라우저 열기
user = User()
site = Site()

class Work :
    def __init__(self):
        driver.get(site.url)
        
    # 로그인 하기
    def login(self) :
        loginId = driver.find_element_by_id(site.put_id)
        loginId.clear()
        loginId.send_keys(user.id)

        loginPassWord = driver.find_element_by_id(site.put_password)
        loginPassWord.clear()
        loginPassWord.send_keys(user.password)

        driver.find_element_by_xpath(site.btnLogin).click()
        
        return


    # 메인->게시판 접근하기
    def moveMainToBoard(self) :
        driver.find_elements_by_css_selector(".m-box2")[1].find_element_by_css_selector(".sub_open").click()
        driver.find_element_by_css_selector("#menu_open_material_16145").click()

        return

    # 현재 날짜 정보 가져오기
    def setTodayMonthDayName(self) :
        now = datetime.now()
        weekday = ["월", "화", "수", "목", "금", "토", "일"]

        name_of_day = weekday[now.weekday()]
        site.title =  f"{now.month}/{now.day}({name_of_day})"
        site.title_complete =  f"{now.month}/{now.day}({name_of_day})"

        return


    # 게시물 생성하기
    def createCheckPost(self):
        button = driver.find_element_by_css_selector(".site_button")
        if (button.text == "글쓰기") :
            button.click()
        else :
            driver.get(site.board_url)
            driver.find_element_by_css_selector(".site_button").click()

        # title
        driver.find_element_by_css_selector(".txttype02").clear()
        driver.find_element_by_css_selector(".txttype02").send_keys(site.title)

        # content
        frame = driver.find_element_by_tag_name("iframe")
        driver.switch_to.frame(frame)
        driver.find_element_by_css_selector("#tinymce").clear()
        driver.find_element_by_css_selector("#tinymce").send_keys(site.content)
        
        #complete
        #driver.find_element_by_css_selector(".site_button_reverse").click()

        return

    ### 가장 최근에 작성한 <출결체크> 게시글 접근
    def moveBoardToNewCheckPost(self):
        try :
            title = driver.find_elements_by_css_selector(".bbslist tbody .left a")
            length = len(driver.find_elements_by_css_selector(".bbslist tbody"))
        except :
            driver.get(site.board_url)
            title = driver.find_elements_by_css_selector(".bbslist tbody .left a")
            length = len(driver.find_elements_by_css_selector(".bbslist tbody"))

        for i in range(length):
            if ("<" in title[i].text) :
                title[i].click()
                break
        
        return

    # 댓글 크롤링
    def crawlComments(self) :
        comment_list = driver.find_elements_by_css_selector(".commentbox .comment-list .comment-name")
        return comment_list

    # 댓글에서 학번만 추출
    def returnStudentId(self, comment_list) :
        result = set()
        for comment in comment_list :
            result.add(comment.text[5:13])

        return result

    # 지각자 결석자 
    def returnResultString(self, s_status):
        result = ""
        s_status.sort()

        for s_id in s_status :
            student = f"{s_id} {student_dict[s_id]} / "
            result += student

        return "해당자 없음" if not result else result[:-2]

    def setResultString(self, late, absent) :
        site.content_complete = (late,absent)
        return

    def createCompletePost(self):
        driver.back()
        button = driver.find_element_by_css_selector(".site_button")
        if (button.text == "글쓰기") :
            button.click()
        else :
            driver.get(site.board_url)
            driver.find_element_by_css_selector(".site_button").click()


        print("??", site.title_complete, site.content_complete)

        # title
        driver.find_element_by_css_selector(".txttype02").clear()
        driver.find_element_by_css_selector(".txttype02").send_keys(site.title_complete)

        # content
        frame = driver.find_element_by_tag_name("iframe")
        driver.switch_to.frame(frame)
        driver.find_element_by_css_selector("#tinymce").clear()
        driver.find_element_by_css_selector("#tinymce").send_keys(site.content_complete)

        #complete
        #driver.find_element_by_css_selector(".site_button_reverse").click()

        return

    def back(self):
        driver.back()

    def forward(self):
        driver.forward()