class pageObjects():
    textBox_username_name = "userName"
    textBox_password_name = "password"
    login_btn_name = "login"
    logout_linkText = "SIGN-OFF"

    def __init__(self, driver):
        self.driver = driver
        print(driver)

    """def setUSerName(self, username):
        self.driver.find_element_by_name(self.textBox_username_name).send_Keys(username)

    def setPassWord(self, password):
        self.driver.find_element_by_name(
            self.textBox_password_name).send_Keys(password)

    def setLogin_btn(self):
        self.driver.find_element_by_name(self.textBox_username_name).click()

    def setLogOut(self):
        self.driver.find_element_by_name(self.textBox_username_name).click()
"""