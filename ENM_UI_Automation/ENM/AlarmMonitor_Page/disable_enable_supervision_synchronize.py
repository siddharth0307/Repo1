from selenium.webdriver.common.action_chains import ActionChains
import time


class SupervisionAndSynchronizationRefresh:
    def __init__(self, driver):
        self.driver = driver
        self.select_first_ne_xpath = "//td[@class='ebTableCell']"
        self.select_to_disable_supervision_xpath = "//div[contains(text(),'Disable Supervision')]"
        self.select_to_enable_supervision_xpath = "//div[contains(text(),'Enable Supervision')]"
        self.select_to_alarm_synchronize_xpath = "//div[contains(text(),'Initiate Alarm Synchronization')]"
        self.select_disable_auto_refresh_xpath = "//span[contains(text(),'Disable Auto Refresh')]"
        self.select_enable_auto_refresh_xpath = "//span[contains(text(),'Enable Auto Refresh')]"

    def disableSuperVision(self):
        ne_to_select = self.driver.find_element_by_xpath(self.select_first_ne_xpath).click()

        action_chains = ActionChains(self.driver)
        action_chains.context_click(ne_to_select).perform()
        time.sleep(2)

        self.driver.find_element_by_xpath(self.select_to_disable_supervision_xpath).click()

    def enableSuperVision(self):
        ne_to_select = self.driver.find_element_by_xpath(self.select_first_ne_xpath).click()

        action_chains = ActionChains(self.driver)
        action_chains.context_click(ne_to_select).perform()
        time.sleep(2)

        self.driver.find_element_by_xpath(self.select_to_enable_supervision_xpath).click()

    def alarmSynchronize(self):
        ne_to_select = self.driver.find_element_by_xpath(self.select_first_ne_xpath).click()

        action_chains = ActionChains(self.driver)
        action_chains.context_click(ne_to_select).perform()

        self.driver.find_element_by_xpath(self.select_to_alarm_synchronize_xpath).click()
        time.sleep(5)

    def autoRefresh(self):
        self.driver.find_element_by_xpath(self.select_disable_auto_refresh_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.select_enable_auto_refresh_xpath).click()
        time.sleep(10)