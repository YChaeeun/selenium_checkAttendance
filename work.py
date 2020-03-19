import userInfo as u
import siteInfo as s

from selenium import webdriver as wd
import urllib

from datetime import datetime

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