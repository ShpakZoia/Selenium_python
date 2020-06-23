import unittest
from selenium import webdriver

class app_test(unittest.TestCase):
    def test_Name(self):
        self.driver = webdriver.Chrome(executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")
        self.driver.get("https://www.google.com/")
        title= self.driver.title
        #self.assertEqual("Google",title,"website tittle is same")
        #self.assertNotEqual("Google",title,"website tittle is same")
        self.assertNotEqual("Google123",title,"website tittle is same")
        
if __name__=="__main__":
    unittest.main()