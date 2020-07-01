from selenium import webdriver
from selenium.webdriver.common import keys
import pytest


class TestOrangeHrm():

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(
            executable_path="E:/SQA/chromedriver_win32/chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_HomePageTitle(self, setup):
        self.driver.get("http://newtours.demoaut.com/")
        self.driver.implicitly_wait(10)
        assert self.driver.title == "Welcome: Mercury Tours"

    def test_Login(self, setup):
        self.driver.get("http://newtours.demoaut.com/")
        self.driver.find_element_by_name("userName").send_keys("mercury")
        self.driver.find_element_by_name("password").send_keys("password")
        self.driver.find_element_by_name("login").click()
        assert self.driver.title == "Sign-on: Mercury Tours"

    def test_run(self):
        print("this is tunning")
