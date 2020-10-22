import time
import unittest
from ENM_UI_Automation.ENM.Login_Page.enmFirstPageNotice import ENMNotice
from ENM_UI_Automation.ENM.Login_Page.enmLoginWithValidCredential import ENMLogin
from ENM_UI_Automation.ENM.Login_Page.enmLoginSuccessfulAfterValidLogin import ENMLoginSuccessfulPage
from ENM_UI_Automation.ENM.ENM_Main_Page.enmHomePage import ENMMainLandingPage
from ENM_UI_Automation.ENM.Read_Write_Data.readInputData import ReadInputData
from ENM_UI_Automation.ENM.Take_Screenshots.screenshot_logic import TakeScreenShot
from selenium.webdriver.common.action_chains import ActionChains
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

    # def test_5_Add_NE_After_Node_Creation(self):
    #     driver = self.driver
    #     add_node_topology_window = ENMAddTopology(driver)
    #     add_found_ne_for_alarm = AddNewNEForAlarm(driver)
    #     view_alarm = ViewAlarmForNode(driver)
    #     take_screen = TakeScreenShot(driver)
    #
    #     # Check if any NE is already applied. If yes, clear it off and then add NE and look for alarm summary.
    #
    #     get_applied_filer_text = driver.find_element_by_css_selector(".eaAlarmviewer-nodeSelection-applied-header").text # This will print the filter value if applied. something like "Applied 5 of 5. Show All Objects".
    #
    #     if "Applied" in get_applied_filer_text:
    #         add_node_topology_window.clearAppliedFilter()
    #         take_screen.take_screen_shot("1_NE_filter_clear")
    #         add_node_topology_window.openTopologyDataWindow()
    #         add_node_topology_window.searchNode()
    #         take_screen.take_screen_shot("2_Node_Searched")
    #         add_node_topology_window.addFoundNode()
    #
    #         add_found_ne_for_alarm.searchNodeInNetwork()
    #         take_screen.take_screen_shot("3_NE_found_for_Alarm_Summary")
    #         add_found_ne_for_alarm.foundNodeInNetwork()
    #
    #         take_screen.take_screen_shot("4_Node_selected_for_alarm_details")
    #         view_alarm.selectAlarmOpenInAnotherTab()
    #         take_screen.take_screen_shot("5_Alarm_Selected_to_view_Summary")
    #         view_alarm.alarmDetailsOnNewTab()
    #         take_screen.take_screen_shot("6_Alarm_Summary_on_new_tab")
    #     else:
    #         add_node_topology_window.openTopologyDataWindow()
    #         add_node_topology_window.searchNode()
    #         take_screen.take_screen_shot("1_Node_Searched")
    #         add_node_topology_window.addFoundNode()
    #
    #         add_found_ne_for_alarm.searchNodeInNetwork()
    #         take_screen.take_screen_shot("2_NE_found_for_Alarm_Summary")
    #         add_found_ne_for_alarm.foundNodeInNetwork()
    #
    #         take_screen.take_screen_shot("3_Node_selected_for_alarm_details")
    #         view_alarm.selectAlarmOpenInAnotherTab()
    #         take_screen.take_screen_shot("4_Alarm_Selected_to_view_Summary")
    #         view_alarm.alarmDetailsOnNewTab()
    #         take_screen.take_screen_shot("5_Alarm_Summary_on_new_tab")

    def test_7_Open_All_Traps_Take_ScreenShot(self):
        driver = self.driver
        take_screen = TakeScreenShot(driver)
        row = len(driver.find_elements_by_xpath("//tbody[@class='elTablelib-Table-body']//tr")) # This finder gives me table length = total no of traps + 3
        total_row = row-3
        print(total_row)
        for trap in range(total_row):
            first_to_last_trap = driver.find_element_by_xpath("//div[@class='elTablelib-Table-wrapper eb_scrollbar']//tbody[1]/tr["+str(trap+1)+"]/td[2]").click()

            action_chains = ActionChains(driver)
            action_chains.double_click(first_to_last_trap).perform()  # Perform Double-Click to open Alarm summary page in new tab.
            driver.switch_to.window(driver.window_handles[trap+1])
            time.sleep(25)
            driver.execute_script("document.body.style.zoom='50%'")
            take_screen.take_screen_shot("Trap_"+str(trap+1)+"_1")

            scroll_down = driver.find_element_by_xpath("//dt[contains(text(),'FMX Generated')]")
            action_chains.move_to_element(scroll_down)
            action_chains.perform()
            time.sleep(1)
            take_screen.take_screen_shot("Trap_" + str(trap+1)+"_2")

            driver.execute_script("document.body.style.zoom='100%'")
            driver.switch_to.window(driver.window_handles[0])




    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Siddharth\\Automation\\ENM_Automation\\ENM_Report"))
