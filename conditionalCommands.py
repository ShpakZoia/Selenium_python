from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")
driver.get("http://thedemosite.co.uk/login.php")
name=driver.find_element_by_name("username")
print(name.is_displayed())
print(name.is_enabled())

password=driver.find_element_by_name("password")
print(password.is_displayed())
print(password.is_enabled())


name.send_keys("himu124")
password.send_keys("himu124")
driver.find_element_by_name("FormsButton2").click()
time.sleep(5)

driver.close()