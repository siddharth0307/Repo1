import time
from ENM_UI_Automation.ENM.Read_Write_Data.readInputData import ReadInputData


class AddNewNEForAlarm:
    def __init__(self, driver):
        self.driver = driver
        self.NE_textbox_xpath = "//div[@class='eaAlarmviewer-nodeSelection-list-default']//input[@placeholder='Type to Find nodes']"
        self.node_name = ReadInputData()
        self.node_text = self.node_name.read_ENM_Node()
        self.click_Find_button_xpath = "//div[@class='eaAlarmviewer-nodeSelection-list-default']//button[@class='ebBtn eaAlarmviewer-nodeList-searchPanel-find'][contains(text(),'Find')]"
        self.click_apply_button_xpath = "//button[contains(@class,'eaAlarmviewer-nodeSelection-footer-apply ebBtn ebBtn_color_paleBlue')]"

    def searchNodeInNetwork(self):
        self.driver.find_element_by_xpath(self.NE_textbox_xpath).send_keys(self.node_text) # Input NE name to be searched.
        self.driver.find_element_by_xpath(self.click_Find_button_xpath).click() # Search to find NE that were added.

    def foundNodeInNetwork(self):
        self.driver.find_element_by_xpath(self.click_apply_button_xpath).click() # Apply the filter with NE selected.
        time.sleep(5)

