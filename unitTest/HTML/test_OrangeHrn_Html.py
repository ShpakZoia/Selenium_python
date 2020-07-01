from selenium import webdriver
import unittest
import HtmlTestRunner


class mercuryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")
        cls.driver.maximize_window()

    def test_HomePageTitle(self):
        self.driver.get("http://newtours.demoaut.com/")
        self.assertEqual("Welcome: Mercury Tours",
                         self.driver.title, "webpage title is matching")

    def test_Login(self):
        self.driver.find_element_by_name("userName").send_keys("mercury")
        self.driver.find_element_by_name("password").send_keys("password")
        self.driver.find_element_by_name("login").click()
        self.assertEqual("Sign-on: Mercury Tours",
                         self.driver.title, "webpage title is matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("closeing Browser")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="..\\Reports"))
