from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source = driver.find_element_by_xpath("//*[@id='box1']")
target = driver.find_element_by_xpath("//*[@id='box101']")

actions = ActionChains(driver)

actions.drag_and_drop(source,target).perform()

time.sleep(3)
driver.quit()