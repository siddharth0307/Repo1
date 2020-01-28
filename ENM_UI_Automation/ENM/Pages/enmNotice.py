class ENMNotice:

    def __init__(self, driver):
        self.driver = driver
        self.loginNoticeId = "loginNoticeOk"

    def clickLoginNotice(self):
        # self.driver.save_screenshot("C:/Siddharth/Automation/ENM_Automation/Screenshots/1.png")
        self.driver.find_element_by_id(self.loginNoticeId).click()