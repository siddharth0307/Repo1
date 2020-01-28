from ENM_UI_Automation.ENM.Pages.enmNotice import ENMNotice
from ENM_UI_Automation.ENM.Pages.enmLogin import ENMLogin
from ENM_UI_Automation.ENM.Pages.enmLoginSuccessful import ENMLoginSuccessfulPage
from ENM_UI_Automation.ENM.Pages.enmHomePage import ENMMainLandingPage
from ENM_UI_Automation.ENM.Pages.enmaddTopology import ENMAddTopology
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ENMAutomation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\Siddharth\Automation\ENM_Automation\drivers\chromedriver.exe")
        # cls.screens = "C:/Siddharth/Automation/ENM_Automation/Screenshots/"
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    def test_1_load_notice_page(self):
        driver = self.driver
        # screens_path = self.screens
        driver.get("https://enmapache.athtem.eei.ericsson.se/login/?goto=https://enmapache.athtem.eei.ericsson.se")
        time.sleep(10)
        driver.save_screenshot("C:/Siddharth/Automation/ENM_Automation/Screenshots/1.png")

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
        time.sleep(5)

    def test_4_ENM_Main_Landing_Page_and_Alarm_Monitor_Click(self):
        driver = self.driver
        alarm_monitor = ENMMainLandingPage(driver)
        alarm_monitor.clickAlarmMonitorLink()
        time.sleep(5)

        applied_filer_text = driver.find_element_by_css_selector(".eaAlarmviewer-nodeSelection-applied-header").text
        if "Applied" in applied_filer_text:
            driver.find_element_by_css_selector(".eaAlarmviewer-nodeSelection-footer-clearAll").click()
            time.sleep(5)
            a = driver.find_element_by_css_selector(".eaAlarmviewer-nodeSelection-header-h4").text
            print("Cleaning selected Network Element. Number of ", a)
            # b = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div[4]/div/div[7]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[2]/table/tbody").text
            # print(b)
            b = driver.find_element_by_css_selector(".elTablelib-Table-body").text
            c = b.split(", ")
            print(c)

        else:
            a = driver.find_element_by_css_selector(".eaAlarmviewer-nodeSelection-header-h4").text
            print("Cleaning selected Network Element. Number of ", a)
            # b = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div[4]/div/div[7]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[2]/table/tbody").text
            # print(b)
            b = driver.find_element_by_css_selector(".elTablelib-Table-body").text
            c = b.split(", ")
            print(c)
            pass

    # def test_5_add_topology(self):
    #     driver = self.driver
    #     open_topology_tab = ENMAddTopology(driver)
    #     open_topology_tab.openTopology()



            # print("will look for specific topology.")
            # l = ["a"]
            #
            # for b in range(1, 2):
            #     a = "/html/body/div[5]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div/div[1]/div/div["
            #     b = str(b)
            #     c = "]/div[3]/div/span"
            #     d = (a+b+c)
            #     e = driver.find_element_by_xpath("\"%s\"" % d)
            #     f = e.text()
            #     l.append(f)
            # print(l)




            # driver.find_element_by_xpath("""/html/body/div[5]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div/div[1]/div/div[8]/div[3]/div/span""").click()
            # text = driver.find_element_by_xpath("""/html/body/div[5]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div/div[1]/div/div[20]/div[3]/div/span""").text
            # print(text)
            # driver.find_element_by_xpath("""/html/body/div[5]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div/div[1]/div/div[20]/div[3]/div/span""").click()
            # print(driver.find_element_by_xpath("//div[8]/div[3]/div/span").text())
            # if driver.find_element_by_xpath("//div[20]/div[3]/div/span").text == None:
            #
            #     window.s
            #     driver.find_element_by_xpath("//div[20]/div[3]/div/span").click()
            #     driver.find_element_by_xpath("//div[20]/div[2]/i").click()
            #     driver.find_element_by_xpath("//div[19]/div[3]/div/span").click()
            #     driver.find_element_by_xpath("//div[3]/div/button/span").click()
            #     print("Inside If statement")
            # else:
            #     driver.find_element_by_xpath("//div[20]/div[3]/div/span").click()
            #     driver.find_element_by_xpath("//div[20]/div[2]/i").click()
            #     driver.find_element_by_xpath("//div[19]/div[3]/div/span")
            #     driver.find_element_by_xpath("//div[3]/div/button/span").click()
            #     print("Inside else statement")
            #
            # time.sleep(5)

            # text = driver.find_element_by_xpath("""/html/body/div[5]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div/div[1]/div/div[8]/div[3]/div/span""").text
            # print(text)
            # text2 = driver.find_element_by_xpath("""xpath=//div[8]/div[3]/div/span""").text
            # print(text2)
            # driver.find_element_by_xpath("//span/div/button/span[2]/i").click()
            # driver.find_element_by_css_selector(".ebComponentList-item ebComponentList-item_focused").click()
            # driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]").text
            # driver.find_element_by_xpath("//div[9]/div[2]/i").click()
            # driver.find_element_by_xpath("//div[9]/div[3]/div/span").click()
            # driver.find_element_by_xpath("//div[9]/div[3]/div/span").click()
            # driver.find_element_by_xpath("//div[3]/div/button/span").click()
            # driver.find_element_by_xpath("//tr[4]/td").click()
            # driver.find_element_by_xpath("//div[4]/button").click()



        time.sleep(10)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


def suite():
    test_suite = unittest.TestSuite()
    # test_suite.addTest(ENMAutomation('test_1_load_notice_page'))
    # test_suite.addTest(ENMAutomation('test_2_login_with_valid_user_credential'))
    # test_suite.addTest(ENMAutomation('test_3_click_on_success_login_page'))
    # test_suite.addTest(ENMAutomation('test_4_ENM_Main_Landing_Page_and_Alarm_Monitor_Click'))
    # test_suite.addTest(ENMAutomation('test_5_add_topology'))
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())

    # unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="C:/Siddharth/Automation/ENM_Automation/ENM_Report"))


