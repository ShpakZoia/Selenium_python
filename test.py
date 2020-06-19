from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(10)

driver.get("https://www.expedia.com/")
driver.find_element_by_css_selector(".uitk-tab-anchor[aria-controls='wizard-flight-pwa']").click()
f_from=driver.find_element_by_css_selector(".uitk-faux-input[aria-label= 'Flying from']")
f_from.send_keys("sfo")
driver.find_element_by_css_selector("[data-stid='location-field-leg1-origin-result-item-button']").click()
time.sleep(2)
driver.find_element_by_css_selector(".uitk-faux-input[aria-label='Flying to']").send_keys("nyc")
driver.find_element_by_css_selector("[data-stid='location-field-leg1-destination-result-item-button']").click()
driver.find_element_by_id("d1-btn").click()

driver.find_element_by_css_selector(".uitk-new-date-picker-day[aria-label='Jun 24, 2020']").send_keys(Keys.ENTER)
driver.find_element_by_css_selector(".uitk-new-date-picker-day[aria-label='Jun 30, 2020']").send_keys(Keys.ENTER)
driver.find_element_by_css_selector("[data-stid='apply-date-picker']").send_keys(Keys.ENTER)
driver.find_element_by_css_selector("[data-testid='submit-button']").send_keys(Keys.ENTER)

wait=WebDriverWait(driver, 10)

a=driver.find_element_by_id("stopFilter_stops-0").click()
e = wait.until(ES.element_to_be_clickable(a))

e.click()