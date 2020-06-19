from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(5)
#driver.switch_to_alert().accept() #accepting the alert
driver.switch_to_alert().dismiss() #dismissing the alert

time.sleep(5)
driver.quit()