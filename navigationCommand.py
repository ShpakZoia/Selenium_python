from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
time.sleep(5)
print(driver.title)



driver.get("https://www.google.com/")
time.sleep(5)
print(driver.title)



driver.back()
time.sleep(5)
print(driver.title)



driver.forward()
time.sleep(5)
print(driver.title)



driver.close()