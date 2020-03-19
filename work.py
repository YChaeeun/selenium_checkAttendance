import userInfo as u
import siteInfo as s
from student import student_list

from selenium import webdriver as wd

from datetime import datetime
import time

user = u.User()  # 유저의 아이디와 비밀번호 정보
site = s.Site()  # 접속하려는 사이트와 관련된 정보 (ex. url, css, class, id)

# 제어할 웹 브라우저 열기
driver = wd.Chrome("./tools/chromedriver.exe")
driver.get(site.url)

# -------------------------------------------------- # 
# 1. 로그인 하기
loginId = driver.find_element_by_id(site.put_id)
loginId.clear()
loginId.send_keys(user.id)

loginPassWord = driver.find_element_by_id(site.put_password)
loginPassWord.clear()
loginPassWord.send_keys(user.password)

driver.find_element_by_xpath(site.btnLogin).click()
# -------------------------------------------------- # 

# -------------------------------------------------- #
# 2. 게시물 올리기
### 게시판 접근하기
driver.find_elements_by_css_selector(".m-box2")[1].find_element_by_css_selector(".sub_open").click()
driver.find_element_by_css_selector("#menu_open_material_16145").click()
driver.find_element_by_css_selector(".site_button").click()

### 글자 입력하기
now = datetime.now()
weekday = ["월", "화", "수", "목", "금", "토", "일"]

name_of_day = weekday[now.weekday()]
site.title = f"{now.month}/{now.day}({name_of_day})"   # ex. 3/19(목)
driver.find_element_by_css_selector(".txttype02").send_keys(site.title)

frame = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(frame)
driver.find_element_by_css_selector("#tinymce").send_keys(site.content)

### 작성완료!
#driver.find_element_by_css_selector(".site_button_reverse").click()

# -------------------------------------------------- #

# -------------------------------------------------- #
# 3. 댓글 크롤링
driver.execute_script("window.history.go(-1)")

### 가장 최근에 작성한 <출결체크> 게시글 접근
title = driver.find_elements_by_css_selector(".bbslist tbody .left a")
length = len(driver.find_elements_by_css_selector(".bbslist tbody"))

for i in range(length):
    if ("<" in title[i].text) :
        title[i].click()
        break

### 16시 31분이 되면 전체 댓글 수집 (출석)
while True :
    now = datetime.now()
    if (now.hour == 16) and (now.minute >= 30) :
        comment_list = driver.find_elements_by_css_selector(".commentbox .comment-list .comment-name")
        break
    else :
        driver.refresh()
        time.sleep(60)

### 지각
for i in range(20) :
    now = datetime.now()
    if (now.hour == 16) and (now.minute >= 45) :
        comment_list_late = driver.find_elements_by_css_selector(".commentbox .comment-list .comment-name")
        break
    else :
        driver.refresh()
        time.sleep(60)
# -------------------------------------------------- #

# -------------------------------------------------- #
# 3-2. 데이터 정제
attendance = set()
late = set()

### 댓글 중 학번만 추출
for comment in comment_list :
    attendance.add(comment.text[5:13])

for comment in comment_list_late :
    late.add(comment.text[5:13])

### 지각자, 결석자
s_late = late - attendance  # 지각자 학번
s_absent = set(student_list) - (attendance | s_late)  # 결석자 학번

# -------------------------------------------------- #