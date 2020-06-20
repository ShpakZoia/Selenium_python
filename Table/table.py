from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")
driver.get("file:///E:/SQA/practice/Selenium_Python/Selenium_python/Table/code.html")

row = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))
col = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))
print(row)
print(col)

print("Product"+"   "+"Article"+"   "+"Price")

for r in range (2,row+1):
    for c in range(1,col+1):
        value = driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]")
        print(value.text,end='   ')
    print()

time.sleep(5)
driver.quit()