import time
from ENM_UI_Automation.ENM.Read_Write_Data.readInputData import ReadInputData


class ENMAddTopology:

    def __init__(self, driver):
        self.driver = driver
        self.applied_filter_on_NE_css = ".eaAlarmviewer-nodeSelection-footer-clearAll"
        self.add_topology_data_xpath = "//span[@class='ebBtn-caption']"
        self.search_tab_xpath = "//div[@class='ebTabs-tabArea']//div[2]//div[1]"
        self.input_node_search_xpath = "//input[@placeholder='Enter Search Criteria']"
        self.click_search_button_xpath = "//i[@class='elNetworkExplorerLib-rSimpleSearch-form-searchBtnIcon ebIcon ebIcon_searchWhite']"
        self.select_checkbox_node_name_xpath = "//div[@class='elTablelib-CheckboxCell-wrap']//input[@class='ebCheckbox']"
        self.click_add_button_xpath = "//button[@class='ebBtn ebBtn_medium ebBtn_color_paleBlue']//span[@class='ebBtn-caption'][contains(text(),'Add')]"
        self.node_name = ReadInputData()
        self.node_text = self.node_name.read_ENM_Node()

    def clearAppliedFilter(self):
        self.driver.find_element_by_css_selector(self.applied_filter_on_NE_css).click()
        time.sleep(10)

    def openTopologyDataWindow(self):
        self.driver.find_element_by_xpath(self.add_topology_data_xpath).click()
        time.sleep(10)

    def searchNode(self):
        self.driver.find_element_by_xpath(self.search_tab_xpath).click()
        time.sleep(5)

        self.driver.find_element_by_xpath(self.input_node_search_xpath).send_keys(self.node_text) # Input Node text to be searched.
        self.driver.find_element_by_xpath(self.click_search_button_xpath).click() # Click Search button
        time.sleep(10)

    def addFoundNode(self):
        self.driver.find_element_by_xpath(self.select_checkbox_node_name_xpath).click()
        self.driver.find_element_by_xpath(self.click_add_button_xpath).click()
        time.sleep(10)
