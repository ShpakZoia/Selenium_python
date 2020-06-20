from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

#scroll by pixel
#driver.execute_script("window.scrollBy(0,500)","")

#scroll till an element is found
#find= driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[2]/tbody/tr[107]/td[2]")
#driver.execute_script("arguments[0].scrollIntoView();",find)

#scroll till the end of the page

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")