from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.switch_to_frame(0)
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C:/Users/Himu/Pictures/Camera Roll/WIN_20200412_01_29_24_Pro.jpg")

time.sleep(3)
driver.quit()