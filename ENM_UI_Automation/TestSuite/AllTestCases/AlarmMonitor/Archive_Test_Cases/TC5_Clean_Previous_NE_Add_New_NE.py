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

        success_login.clickSubmitButton()
        time.sleep(5)

    def test_4_ENM_Main_Landing_Page_and_Click_Alarm_Monitor(self):
        driver = self.driver
        alarm_monitor = ENMMainLandingPage(driver)

        alarm_monitor.clickAlarmMonitorLink()
        time.sleep(20)

    def test_5_Add_NE_After_Node_Creation(self):
        driver = self.driver
        add_node_topology_window = ENMAddTopology(driver)
        add_found_ne_for_alarm = AddNewNEForAlarm(driver)
        total_ne_count = CheckNEAvailable(driver)
        get_to_clean_nes = CleanAllOldNEs(driver)

        # This will print the filter value if applied. something like "Applied 5 of 5. Show All Objects".
        get_applied_filer_text = driver.find_element_by_css_selector(".eaAlarmviewer-nodeSelection-applied-header").text

        if "Applied" in get_applied_filer_text:
            print("in if statement")
            driver.find_element_by_xpath("//button[@class='eaAlarmviewer-nodeSelection-footer-clearAll ebBtn']").click()
            time.sleep(5)

            get_to_clean_nes.cleanAllNEs()

            add_node_topology_window.openTopologyDataWindow()
            add_node_topology_window.searchNode()
            add_node_topology_window.addFoundNode()

            add_found_ne_for_alarm.searchNodeInNetwork()
            add_found_ne_for_alarm.foundNodeInNetwork()

        elif total_ne_count.countTotalNEs() == 0:
            print("in elif statement")
            add_node_topology_window.openTopologyDataWindow()
            add_node_topology_window.searchNode()
            add_node_topology_window.addFoundNode()

            add_found_ne_for_alarm.searchNodeInNetwork()
            add_found_ne_for_alarm.foundNodeInNetwork()
        else:
            print("in else statement")
            get_to_clean_nes.cleanAllNEs()

            add_node_topology_window.openTopologyDataWindow()
            add_node_topology_window.searchNode()
            add_node_topology_window.addFoundNode()

            add_found_ne_for_alarm.searchNodeInNetwork()
            add_found_ne_for_alarm.foundNodeInNetwork()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Siddharth\\Automation\\ENM_Automation\\ENM_Report"))
