from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

doubleClick = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

action = ActionChains(driver)

action.double_click(doubleClick).perform()