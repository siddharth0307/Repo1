class ENMLogin:

    def __init__(self, driver):
        self.driver = driver
        self.userLoginId = "loginUsername"
        self.userPasswordId = "loginPassword"
        self.clickbuttonid = "submit"

    def enterUsername(self, username):
        self.driver.find_element_by_id(self.userLoginId).clear()
        self.driver.find_element_by_id(self.userLoginId).send_keys(username)

    def enterUserPassword(self, password):
        self.driver.find_element_by_id(self.userPasswordId).clear()
        self.driver.find_element_by_id(self.userPasswordId).send_keys(password)

    def clickbutton(self):
        # self.driver.save_screenshot("C:/Siddharth/Automation/ENM_Automation/Screenshots/2.png")
        self.driver.find_element_by_id(self.clickbuttonid).click()