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


class TrapTesting(unittest.TestCase):

    # Pre-condition

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

    def test_2_login_with_valid_user_credential(self):
        driver = self.driver
        username = ReadInputData()
        login = ENMLogin(driver)

        user_name_text = username.read_ENM_User_Name()
        user_pass_text = username.read_ENM_User_Pass()

        login.enterUsername(user_name_text)
        login.enterUserPassword(user_pass_text)
        login.clickbutton()
        time.sleep(10)

    def test_3_click_on_Logon_Success_Page_After_Valid_login(self):
        driver = self.driver
        success_login = ENMLoginSuccessfulPage(driver)

        success_login.clickSubmitButton()
        time.sleep(15)

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
            driver.find_element_by_xpath("//button[@class='eaAlarmviewer-nodeSelection-footer-clearAll ebBtn']").click()
            time.sleep(10)

            get_to_clean_nes.cleanAllNEs()

            add_node_topology_window.openTopologyDataWindow()
            add_node_topology_window.searchNode()
            add_node_topology_window.addFoundNode()

            add_found_ne_for_alarm.searchNodeInNetwork()
            add_found_ne_for_alarm.foundNodeInNetwork()

        elif total_ne_count.countTotalNEs() == 0:
            add_node_topology_window.openTopologyDataWindow()
            add_node_topology_window.searchNode()
            add_node_topology_window.addFoundNode()

            add_found_ne_for_alarm.searchNodeInNetwork()
            add_found_ne_for_alarm.foundNodeInNetwork()
        else:
            get_to_clean_nes.cleanAllNEs()

            add_node_topology_window.openTopologyDataWindow()
            add_node_topology_window.searchNode()
            add_node_topology_window.addFoundNode()

            add_found_ne_for_alarm.searchNodeInNetwork()
            add_found_ne_for_alarm.foundNodeInNetwork()

    def test_6_Disable_Enable_Supervision_Generate_Trap_Browser_Refresh_Take_ScreenShot(self):
        driver = self.driver
        supervision_sync_refresh = SupervisionAndSynchronizationRefresh(driver)
        take_screen = TakeScreenShot(driver)

        supervision_sync_refresh.disableSuperVision()
        time.sleep(5)
        take_screen.take_screen_shot("Disable_Supervision")
        print("Supervision has been disabled.")

        supervision_sync_refresh.enableSuperVision()
        time.sleep(5)
        take_screen.take_screen_shot("Enable_Supervision")
        print("Supervision has been enabled.")

        print("Please Generate traps. Script will wait for 3 minutes only....")
        time.sleep(180)
        print("3 minutes over. Starting to capture screenshots of all traps")
        supervision_sync_refresh.autoRefresh()
        take_screen.take_screen_shot("After_Refresh")
        print("Browser Refresh done.")


    def test_7_Open_All_Traps_Take_ScreenShot(self):
        driver = self.driver
        take_screen = TakeScreenShot(driver)

        trap_row = len(driver.find_elements_by_xpath("//tbody[@class='elTablelib-Table-body']//tr")) # This finder gives table length = total no of traps + 1
        total_trap_row = trap_row-1
        print(total_trap_row)
        for trap in range(total_trap_row):
            first_to_last_trap = driver.find_element_by_xpath("//div[@class='elTablelib-Table-wrapper eb_scrollbar']//tbody[1]/tr["+str(trap+1)+"]/td[2]").click()

            action_chains = ActionChains(driver)
            action_chains.double_click(first_to_last_trap).perform()  # Perform Double-Click to open Alarm summary page in new tab.
            time.sleep(10)
            driver.switch_to.window(driver.window_handles[trap+1])
            driver.execute_script("document.body.style.zoom='50%'")
            time.sleep(40)
            take_screen.take_screen_shot("Trap_"+str(trap+1)+"_1")

            scroll_down = driver.find_element_by_xpath("//dt[contains(text(),'FMX Generated')]")
            action_chains.move_to_element(scroll_down)
            action_chains.perform()
            time.sleep(10)
            take_screen.take_screen_shot("Trap_" + str(trap+1)+"_2")

            driver.execute_script("document.body.style.zoom='100%'")
            driver.switch_to.window(driver.window_handles[0])

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Siddharth/Automation/ENM_Automation/Output/ENM_Report"))
