import unittest
from ENM_UI_Automation.TestSuite.AllTestCases.AlarmMonitor.Archive_Test_Cases.TC1_Open_ENM_Page_Close_Browser import OpenENMPage
from ENM_UI_Automation.TestSuite.AllTestCases.AlarmMonitor.Archive_Test_Cases.TC2_Login_with_Valid_Credentials import ValidLogin

# Get all test cases
tc1 = unittest.TestLoader().loadTestsFromTestCase(OpenENMPage)
tc2 = unittest.TestLoader().loadTestsFromTestCase(ValidLogin)

# Create Test Suite

sanityTest = unittest.TestSuite([tc1, tc2])

# Execute the one you want and rest is commented.

unittest.TextTestRunner().run(sanityTest)
