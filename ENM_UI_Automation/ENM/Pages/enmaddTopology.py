class ENMAddTopology:

    def __init__(self, driver):
        self.driver = driver
        self.add_topology_css = ".ebBtn-caption"
        self.click_topology_tab_css = ".ebTabs-tabItem_selected_true"
        self.click_drop_down_css = ".ebSelect-iconHolder > .ebIcon"
        self.select_network_Data_css = ".ebComponentList-item_focused"

    def openTopology(self):
        self.driver.find_element_by_css_selector(self.add_topology_css).click()  # Click Add Topology
        self.driver.find_element_by_css_selector(self.click_topology_tab_css).click()  # Click on Topology Tab
        self.driver.find_element_by_css_selector(self.click_drop_down_css).click()  # Click on Drop down items
        self.driver.find_element_by_css_selector(self.select_network_Data_css).click()  # Selects the Network Data

