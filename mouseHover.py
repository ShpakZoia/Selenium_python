from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//*[@id='btnLogin']").click()

actions = ActionChains(driver)

admin= driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']")
userManagement = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
users = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

actions.move_to_element(admin).move_to_element(userManagement).move_to_element(users).click().perform()

time.sleep(10)
driver.quit()