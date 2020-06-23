import unittest
from selenium import webdriver

class app_test(unittest.TestCase):
    def test_app_Name(self):
        self.driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")
        #self.assertIsNone(self.driver)
        self.assertIsNotNone(self.driver)

if __name__=="__main__":
    unittest.main()