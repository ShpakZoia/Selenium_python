from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")

driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium.ie").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("packageFrame")
driver.find_element_by_xpath("/html/body/div/ul[2]/li[1]/a").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]").click()
time.sleep(3)

driver.quit()