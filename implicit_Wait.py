from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")

driver.implicitly_wait(10)

driver.get("http://thedemosite.co.uk/login.php")

driver.find_element_by_name("username").send_keys("himu124")
driver.find_element_by_name("password").send_keys("himu124")
driver.find_element_by_name("FormsButton2").click()
time.sleep(5)

driver.close()