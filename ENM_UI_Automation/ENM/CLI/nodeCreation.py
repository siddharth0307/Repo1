import time
import unittest
from ENM_UI_Automation.ENM.Login_Page.enmFirstPageNotice import ENMNotice
from ENM_UI_Automation.ENM.Login_Page.enmLoginWithValidCredential import ENMLogin
from ENM_UI_Automation.ENM.Login_Page.enmLoginSuccessfulAfterValidLogin import ENMLoginSuccessfulPage
from selenium import webdriver
import HtmlTestRunner


class ValidLogin(unittest.TestCase):

# Pre-condition

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\Siddharth\Automation\ENM_Automation\drivers\chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.url = "https://enmapache.athtem.eei.ericsson.se/login/?goto=https://enmapache.athtem.eei.ericsson.se"

# Actual Test

    def test_1_load_notice_page(self):
        driver = self.driver
        # screens_path = self.screens
        driver.get(self.url)
        time.sleep(10)
        # driver.save_screenshot("C:/Siddharth/Automation/ENM_Automation/Screenshots/1.png")

        notice = ENMNotice(driver)
        notice.clickLoginNotice()

    def test_2_login_with_valid_user_credential(self):
        driver = self.driver
        login = ENMLogin(driver)
        login.enterUsername("administrator")
        login.enterUserPassword("TestPassw0rd")
        login.clickbutton()
        time.sleep(5)

    def test_3_click_on_success_login_page(self):
        driver = self.driver
        success_login = ENMLoginSuccessfulPage(driver)
        success_login.clickSubmitButton()
        time.sleep(10)

    def test_4_click_CLI(self):
        driver = self.driver
        driver.find_element_by_xpath("//a[contains(text(),'Command Line Interface')]").click()
        time.sleep(10)



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Siddharth\\Automation\\ENM_Automation\\ENM_Report"))
