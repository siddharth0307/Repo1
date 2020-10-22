from selenium.webdriver.common.action_chains import ActionChains
import time


class CleanAllOldNEs:
    def __init__(self, driver):
        self.driver = driver
        self.find_ne_with_css = ".elTablelib-Table-body"
        self.select_first_ne_xpath = "//td[@class='ebTableCell']"
        self.select_to_remove_from_list_xpath = "//div[contains(text(),'Remove From List')]"

    def cleanAllNEs(self):
        get_all_available_nes = self.driver.find_element_by_css_selector(self.find_ne_with_css).text
        convert_to_list = ''.join((map(str, get_all_available_nes)))
        final_ne_available = convert_to_list.split('\n')
        # print(final_ne_available)

        len_of_ne_list = len(final_ne_available)
        for each_ne in range(len_of_ne_list):
            ne_to_select = self.driver.find_element_by_xpath(self.select_first_ne_xpath).click()

            action_chains = ActionChains(self.driver)
            action_chains.context_click(ne_to_select).perform()
            time.sleep(1)

            self.driver.find_element_by_xpath(self.select_to_remove_from_list_xpath).click()
            time.sleep(10)