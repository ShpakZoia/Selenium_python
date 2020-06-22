import utilityxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()
path = "E:/SQA/practice/Selenium_Python/Selenium_python/excel/DataDriven.xlsx"

rows = utilityxl.rowCount(path,"Sheet1")

for r in range (2 , rows+1):
    username = utilityxl.readData(path,"Sheet1", r , 1)
    pasword = utilityxl.readData(path,"Sheet1", r , 2)
    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(pasword)
    
    driver.find_element_by_name("login").click()
  
    time.sleep(10)
    print(driver.title)

    if (driver.title=="Find a Flight: Mercury Tours:"):
        utilityxl.writeData(path,"Sheet1",r,3,"Test Passed")
        print("Test Passed")

    elif (time.sleep(11)):
        try:
            myElem = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.link_text, 'SIGN-OFF')))
            print ("Page is ready!")
            utilityxl.writeData(path,"Sheet1",r,3,"Test took more time")
        except TimeoutException:
            print ("Loading took too much time!")
    
    elif (driver.title=="Sign-on: Mercury Tours"):
        
        print("test failed")
        utilityxl.writeData(path,"Sheet1",r,3,"test failed")
    
    driver.find_element_by_link_text("Home").click()
    
driver.quit()

    