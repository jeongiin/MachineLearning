
from urllib.request import urlretrieve
from urllib.parse import quote_plus
from bs4 import  BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time


search = '멧돼지'
url = 'https://www.google.com/search?q='+search+'&sxsrf=ALeKk00-LJmbbpnm-KxWK-dyt94QCJ-LkA:1591957148008&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjRvrfChvzpAhUuy4sBHfxfD6YQ_AUoAXoECBcQAw&cshid=1591957257312238&biw=1624&bih=824&dpr=1.13'

driver = webdriver.Chrome('D:\Downloads\chromedriver_win32 (2)\chromedriver.exe') #자신의 경로로 바꿔줘야함
driver.get(url)

# google 이미지 데이터를 다량 수집하기 위한 꼼수
body = driver.find_element_by_tag_name('body')  # 스크롤하기 위한 소스

# range에 page 번호 작성 여러번 내려갈수록 많이 불러옴
for vindex in range(5):
    body.send_keys((Keys.END))
    time.sleep(1)
body.send_keys(Keys.HOME)  # 홈 키로 최상단
##############################################

html = driver.page_source
soup = BeautifulSoup(html, features="html.parser")

img = soup.find_all("img", class_ = "rg_i Q4LuWd")
#img = soup.select('.rg_i.Q4LuWd')

n=1
imgurl = []


for i in img:
    try:
        imgurl.append(i.attrs["src"])

    except KeyError:
        imgurl.append(i.attrs["data-src"])

#print(len(imgurl))
# train : val : test = 6 : 2: 2 로 맞추고자 함
for i in imgurl:
    if n < 71:
        urlretrieve(i, "./크롤링 사진/" + search + "/train/" + search + str(n) + ".jpg")
    elif n < 91:
        urlretrieve(i, "./크롤링 사진/" + search + "/val/" + search + str(n) + ".jpg")
    elif n < 111:
        urlretrieve(i, "./크롤링 사진/" + search + "/test/" + search + str(n) + ".jpg")
    else:
        urlretrieve(i, "./크롤링 사진/" + search + "/" + search + str(n) + ".jpg")

    n+=1

# for i in range(60):
#     try :


driver.close()

