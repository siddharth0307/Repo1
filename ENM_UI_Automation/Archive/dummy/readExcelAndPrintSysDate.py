import time
import unittest
from selenium import webdriver
import HtmlTestRunner
import xlrd

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
        system_time = time.strftime("%d_%m_%Y")
        print(system_time)
        read_file_location = xlrd.open_workbook("C:\Siddharth\Automation\ENM_Automation\ENM_UI_Automation\ReadWriteFile\ENM_Data.xlsx")
        sheet = read_file_location.sheet_by_index(0)
        print(sheet.cell(0, 0))



        # driver.save_screenshot("C:/Siddharth/Automation/ENM_Automation/Screenshots/1.png")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Siddharth\\Automation\\ENM_Automation\\ENM_Report"))
