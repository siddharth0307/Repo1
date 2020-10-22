import time
import unittest
from ENM_UI_Automation.ENM.Login_Page.enmFirstPageNotice import ENMNotice
from ENM_UI_Automation.ENM.Login_Page.enmLoginWithValidCredential import ENMLogin
from ENM_UI_Automation.ENM.Take_Screenshots.screenshot_logic import TakeScreenShot
from ENM_UI_Automation.ENM.Read_Write_Data.readInputData import ReadInputData
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
        driver.get(self.url)
        time.sleep(10)

        notice = ENMNotice(driver)
        notice.clickLoginNotice()

    def test_2_login_with_valid_user_credential(self):
        driver = self.driver
        username = ReadInputData()
        take_screen = TakeScreenShot(driver)
        login = ENMLogin(driver)

        user_name_text = username.read_ENM_User_Name()
        user_pass_text = username.read_ENM_User_Pass()

        login.enterUsername(user_name_text)
        login.enterUserPassword(user_pass_text)

        take_screen.take_screen_shot("Login_Input_Page")

        login.clickbutton()
        time.sleep(5)

    # Tear Down - Close Browser

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Siddharth\\Automation\\ENM_Automation\\ENM_Report"))
