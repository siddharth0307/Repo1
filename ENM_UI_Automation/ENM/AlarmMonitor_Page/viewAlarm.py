from selenium.webdriver.common.action_chains import ActionChains
from ENM_UI_Automation.ENM.Read_Write_Data.readInputData import ReadInputData
import time


class ViewAlarmForNode:
    def __init__(self, driver):
        self.driver = driver
        self.find_first_NE_of_Alarm_xpath = "//div[@class='elTablelib-Table-wrapper eb_scrollbar']//tr[1]//td[2]"
        self.fdn_value_xpath = "//dd[@class='eaAlarmdetails-AdditionalInformation-definitionListDefinition'][contains(text(),'NetworkElement=IVR')]"
        self.node_name = ReadInputData()
        self.node_text = self.node_name.read_ENM_Node()
        self.fdn_actual_text = self.node_name.read_fdn_value_to_compare()

    def selectAlarmOpenInAnotherTab(self):
        get_first_element = self.driver.find_element_by_xpath(self.find_first_NE_of_Alarm_xpath)
        get_first_element.click()  # This click will just select the first alarm

        action_chains = ActionChains(self.driver)
        action_chains.double_click(get_first_element).perform()  # Perform Double-Click to open Alarm summary page in new tab.
        time.sleep(20)

    def alarmDetailsOnNewTab(self):
        print("These are list of total tabs: ", self.driver.switch_to.window)
        self.driver.switch_to.window(self.driver.window_handles[1])
        fdn_text = self.driver.find_element_by_xpath(self.fdn_value_xpath).text
        print(fdn_text)

        if fdn_text == self.fdn_actual_text:
            print("Value match 100%")
        else:
            print("Value did not match")