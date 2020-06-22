from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()

#driver.save_screenshot("E:/SQA/practice/Selenium_Python/Selenium_python/screenshot/test.png")
driver.get_screenshot_as_file("E:/SQA/practice/Selenium_Python/Selenium_python/screenshot/test2.png")
time.sleep(2)
driver.quit()
