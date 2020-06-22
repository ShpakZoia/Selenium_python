import utilityxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
driver.maximize_window()
path = "E:/SQA/practice/Selenium_Python/Selenium_python/excel/DataDriven.xlsx"

rows = utilityxl.rowCount(path,"Sheet1")

for r in range (2 , rows+1):
    username = utilityxl.readData(path,"Sheet1", r , 1)
    pasword = utilityxl.readData(path,"Sheet1", r , 2)
    driver.find_element_by_id("txtUsername").send_keys(username)
    driver.find_element_by_id("txtPassword").send_keys(pasword)
    
    driver.find_element_by_id("btnLogin").click()
    time.sleep(5)

    print(driver.title)

    if (driver.title=="OrangeHRM"):
        utilityxl.writeData(path,"Sheet1",r,3,"Test Passed")
        print("Test Passed")
    
    else:
        print("test failed")
        utilityxl.writeData(path,"Sheet1",r,3,"test failed")
    
    driver.find_element_by_id("welcome").click()
    driver.find_element_by_link_text("Logout").click()
    

    