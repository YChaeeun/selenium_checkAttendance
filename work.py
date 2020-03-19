import userInfo as u
import siteInfo as s

from selenium import webdriver as wd
import urllib

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