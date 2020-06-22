from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")
driver.get("https://www.amazon.com/")
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

cookie = {'name' : 'foo', 'value' : 'bar'}
driver.add_cookie(cookie)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

driver.delete_cookie('foo')
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)