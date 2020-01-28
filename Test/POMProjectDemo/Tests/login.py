from Test.POMProjectDemo.Pages.loginPage import LoginPage
from Test.POMProjectDemo.Pages.homePage import HomePage
# import os
# import sys
import time
import unittest
from selenium import webdriver
import HtmlTestRunner
# sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))



class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\Siddharth\Automation\ENM_Automation\drivers\chromedriver.exe")
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        welcome_menu = driver.find_element_by_xpath("""// *[ @ id = "welcome"]""")
        if driver.find_element_by_xpath("""// *[ @ id = "welcome"]""") == welcome_menu:
            print("xpath found.")
            homepage.click_welcome()
        else:
            time.sleep(60)
            homepage.click_logout()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Siddharth/Automation/ENM_Automation/report"))
