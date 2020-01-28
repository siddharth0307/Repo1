class HomePage:
    def __init__(self, driver):
        self.driver = driver

        # self.welcome_link_id = "welcome"
        # self.logout_link_linkTest = "Logout"
        self.welcome_link_xpath = """// *[ @ id = "welcome"]"""
        self.logout_link_xpath = """//*[@id="welcome-menu"]/ul/li[2]/a"""

    def click_welcome(self):
        self.driver.find_element_by_xpath(self.welcome_link_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()


