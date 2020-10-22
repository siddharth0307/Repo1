
class CheckNEAvailable:
    def __init__(self, driver):
        self.driver = driver
        self.find_no_of_ne_available_xpath = "//h4[@class='eaAlarmviewer-nodeSelection-header-h4']"

    def countTotalNEs(self):
        total_ne_available = self.driver.find_element_by_xpath(self.find_no_of_ne_available_xpath).text
        get_list = list(total_ne_available)
        return int(get_list[-2])