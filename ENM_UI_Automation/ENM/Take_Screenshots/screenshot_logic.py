import time
import xlrd


class TakeScreenShot:

    def __init__(self, driver):
        self.driver = driver
        self.screens = "C:/Siddharth/Automation/ENM_Automation/Output/Screenshots/"
        self.input_file_path = "C:\Siddharth\Automation\ENM_Automation\Input\ENM_Data.xlsx"

    def take_screen_shot(self, filename):
        read_file_location = xlrd.open_workbook(self.input_file_path)
        sheet = read_file_location.sheet_by_index(0)
        node_name = sheet.cell(1, 2)

        system_time = time.strftime("%d_%m_%Y_%H_%M_%S")
        self.driver.save_screenshot("{}{}_{}_{}.png".format(self.screens, node_name.value, filename, system_time))
