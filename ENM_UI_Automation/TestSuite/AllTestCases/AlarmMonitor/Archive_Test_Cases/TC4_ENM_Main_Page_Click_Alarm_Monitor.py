import time
import unittest
from ENM_UI_Automation.ENM.Login_Page.enmFirstPageNotice import ENMNotice
from ENM_UI_Automation.ENM.Login_Page.enmLoginWithValidCredential import ENMLogin
from ENM_UI_Automation.ENM.Login_Page.enmLoginSuccessfulAfterValidLogin import ENMLoginSuccessfulPage
from ENM_UI_Automation.ENM.ENM_Main_Page.enmHomePage import ENMMainLandingPage
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
        time.sleep(5)

        notice = ENMNotice(driver)
        notice.clickLoginNotice()

    def test_2_login_with_valid_user_credential(self):
        driver = self.driver
        username = ReadInputData()
        login = ENMLogin(driver)

        user_name_text = username.read_ENM_User_Name()
        user_pass_text = username.read_ENM_User_Pass()

        login.enterUsername(user_name_text)
        login.enterUserPassword(user_pass_text)
        login.clickbutton()
        time.sleep(5)

    def test_3_click_on_Logon_Success_Page_After_Valid_login(self):
        driver = self.driver
        success_login = ENMLoginSuccessfulPage(driver)
        take_screen = TakeScreenShot(driver)

        success_login.clickSubmitButton()
        time.sleep(5)

    def test_4_ENM_Main_Landing_Page_and_Click_Alarm_Monitor(self):
        driver = self.driver
        alarm_monitor = ENMMainLandingPage(driver)
        take_screen = TakeScreenShot(driver)

        take_screen.take_screen_shot("ENM_Application_Launcher_Page")
        alarm_monitor.clickAlarmMonitorLink()
        time.sleep(20)
        take_screen.take_screen_shot("Alarm_Monitor_Page")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Siddharth\\Automation\\ENM_Automation\\ENM_Report"))
