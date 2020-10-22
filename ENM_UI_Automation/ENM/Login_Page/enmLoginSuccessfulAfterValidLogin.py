class ENMLoginSuccessfulPage:

    def __init__(self, driver):
        self.driver = driver
        self.submitButtonId = "continueButton"

    def clickSubmitButton(self):
        # self.driver.save_screenshot("C:/Siddharth/Automation/ENM_Automation/Screenshots/3.png")
        self.driver.find_element_by_id(self.submitButtonId).click()
