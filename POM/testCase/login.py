from page.pageObject import pageObjects
from selenium import webdriver
import unittest
import HtmlTestRunner
import sys
import time
sys.path.append("E:/SQA/practice/Selenium_Python/Selenium_python/POM")


class logInTest(unittest.TestCase):
    username = "mercury"
    password = "mercury"
    web_address = "http://newtours.demoaut.com/"

    driver = webdriver.Chrome(
        executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.web_address)
        cls.driver.maximize_window()

    def test_Login(self):
        po = pageObjects(self.driver)
        po.setUSerName(self.username)
        po.setPassWord(self.password)
        po.setLogin_btn()
        time.sleep(10)
        self.assertEqual("Find a Flight: Mercury Tours:",
                         self.driver.title, "Title not matched")
        po.setLogOut()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="..\\Reports"))
