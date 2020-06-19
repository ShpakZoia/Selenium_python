from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
links=driver.find_elements_by_tag_name("a")
print(len(links))

for link in links:
    print(link.text)

driver.find_element_by_link_text("REGISTER").click()
time.sleep(3)
driver.find_element_by_partial_link_text("SUPP").click()
time.sleep(5)

driver.quit()