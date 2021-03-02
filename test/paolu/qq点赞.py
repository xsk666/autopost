# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# 模拟浏览器打开网站
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
driver.get("http://8dsw8.com/?cid=1&tid=42")
WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, "inputvalue")))
driver.find_element_by_id("inputvalue").send_keys("3104182180")
driver.find_element_by_id("submit_buy").click()
