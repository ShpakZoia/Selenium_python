from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory" : "C:/Users/Himu/Downloads"})
driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe",options=chromeOptions)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

driver.find_element_by_id("textbox").send_keys("hello sire!")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()


driver.find_element_by_id("pdfbox").send_keys("hello sire!")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()

time.sleep(5)