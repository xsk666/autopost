# coding=utf-8
import time,requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# 模拟浏览器打开网站
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
# window电脑本地
# driver = webdriver.Chrome("./chromedriver.exe")
driver.get("http://8dsw8.com/")
driver.find_element_by_xpath("//option[contains(text(),'『福利』免费活动区')]").click()
time.sleep(1)
driver.find_elements_by_tag_name("option")[56].click()
time.sleep(0.5)
driver.find_element_by_id("inputvalue").send_keys("3104182180")
time.sleep(0.5)
driver.find_element_by_id("submit_buy").click()
print("点赞成功")
# requests.get("https://sc.ftqq.com/SCU79675Tbfd23351bd3ed5501aae715beddfbdbf5e3a123f8fb98.send?text=每日QQ点赞成功&desp=时间为" +time.strftime("%Y/%m/%d")).json()

