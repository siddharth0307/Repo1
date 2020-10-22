import time
import unittest
from ENM_UI_Automation.ENM.Login_Page.enmFirstPageNotice import ENMNotice
from ENM_UI_Automation.ENM.Login_Page.enmLoginWithValidCredential import ENMLogin
from ENM_UI_Automation.ENM.Login_Page.enmLoginSuccessfulAfterValidLogin import ENMLoginSuccessfulPage
from ENM_UI_Automation.ENM.ENM_Main_Page.enmHomePage import ENMMainLandingPage
from ENM_UI_Automation.ENM.Read_Write_Data.readInputData import ReadInputData
from ENM_UI_Automation.ENM.AlarmMonitor_Page.enmaddTopology import ENMAddTopology
from ENM_UI_Automation.ENM.AlarmMonitor_Page.add_NE_To_View_Alarm import AddNewNEForAlarm
from ENM_UI_Automation.ENM.AlarmMonitor_Page.findIfNeAvailable import CheckNEAvailable
from ENM_UI_Automation.ENM.AlarmMonitor_Page.clean_All_Old_NEs_Before_Adding_NE import CleanAllOldNEs
from ENM_UI_Automation.ENM.AlarmMonitor_Page.disable_enable_supervision_synchronize import SupervisionAndSynchronizationRefresh
from selenium.webdriver.common.action_chains import ActionChains
from ENM_UI_Automation.ENM.Take_Screenshots.screenshot_logic import TakeScreenShot
from selenium import webdriver
import HtmlTestRunner

class OpenENMPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\Siddharth\Automation\ENM_Automation\ENM_UI_Automation\drivers\chromedriver.exe")
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

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Siddharth/Automation/ENM_Automation/Output/ENM_Report"))
