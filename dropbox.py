from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
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
value=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(value)
driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[1]/td/label").click()
value = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(value)

checkbox = driver.find_element_by_id("RESULT_CheckBox-8_1").is_selected()
print(checkbox)
driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[1]/td/label").click()
driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[6]/td/label").click()

element = driver.find_element_by_id("RESULT_RadioButton-9")
drp = Select(element)
drp.select_by_index(2)
time.sleep(1)
drp.select_by_value("Radio-0")
time.sleep(1)
drp.select_by_visible_text("Evening")
time.sleep(1)
print(len(drp.options))
all_options= drp.options
for option in all_options:
    print(option.text)
time.sleep(10)
driver.quit()