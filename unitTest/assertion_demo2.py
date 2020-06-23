import unittest
from selenium import webdriver

class app_test(unittest.TestCase):
    def test_app_Name(self):
        self.driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")
        self.driver.get("https://www.facebook.com/")
        title=self.driver.title
        #self.assertTrue("Facebook – log in or sign up"==title)
        #self.assertFalse("Facebook – log in or sign up"==title)
        self.assertFalse("Facebook – log in or sign up1"==title)

if __name__=="__main__":
    unittest.main()