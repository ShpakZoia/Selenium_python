from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome (executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")

driver.get("https://www.facebook.com/")
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath("//*[@id='u_0_b']").click()
time.sleep(5)

driver.quit()