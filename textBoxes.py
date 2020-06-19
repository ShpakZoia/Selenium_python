from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

textBoxes = driver.find_elements_by_class_name("text_field")
print(len(textBoxes))
driver.find_element_by_id("RESULT_TextField-1").send_keys("shamiul")
driver.find_element_by_id("RESULT_TextField-2").send_keys("islam")
driver.find_element_by_id("RESULT_TextField-3").send_keys("017000000000")
driver.find_element_by_id("RESULT_TextField-4").send_keys("bangladesh")
driver.find_element_by_id("RESULT_TextField-5").send_keys("dhaka")
driver.find_element_by_id("RESULT_TextField-6").send_keys("lol@lol.com")
time.sleep(10)
driver.quit()