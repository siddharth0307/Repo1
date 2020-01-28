class ENMMainLandingPage:

    def __init__(self, driver):
        self.driver = driver
        self.AlarmMonitorText = "Alarm Monitor (FM)"

    def clickAlarmMonitorLink(self):
        self.driver.find_element_by_link_text(self.AlarmMonitorText).click()