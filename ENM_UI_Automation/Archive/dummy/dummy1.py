# from ENM_UI_Automation.ENM.Read_Write_Data.readInputData import ReadDataFromFile
#
# user_name = ReadDataFromFile()
# print("Hello " + str(user_name.read_ENM_User_Name()))
# import os
#
# os.system("pip list")

# list = ['JUN-NODE-1\nJUN-NODE-2']
#
# listToStr = ''.join((map(str, list)))
#
# a = listToStr.split('\n')
# print(a)
# # i=0
# for i in range (len(a)):
#     print(a[i])

from selenium import webdriver
import time

driver = webdriver.Chrome("C:\Siddharth\Automation\ENM_Automation\drivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://enmapache.athtem.eei.ericsson.se/login/?goto=https://enmapache.athtem.eei.ericsson.se")
time.sleep(10)

