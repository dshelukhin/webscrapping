from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

site_url = 'https://www.dtccdata.com/'
file1_url = 'https://www.dtccdata.com/api/sitecore/TIWReports/ExportFile?reporttypeitem=06490868-5b65-459a-b676-901e59a95680&tablename=Table3&weekdate=20180904&sectionname=Section%201'
file2_url = 'https://www.dtccdata.com/api/sitecore/TIWReports/ExportFile?reporttypeitem=06490868-5b65-459a-b676-901e59a95680&tablename=Table4&weekdate=20180904&sectionname=Section%201'
file3_url = 'https://www.dtccdata.com/api/sitecore/TIWReports/ExportFile?reporttypeitem=06490868-5b65-459a-b676-901e59a95680&tablename=Section%20IV%20Single%20Names&weekdate=20180904&sectionname=Section%204'

username = '*'
password = '*'

option = webdriver.ChromeOptions()
option.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=option)
driver.get(site_url)

driver.find_element_by_xpath('//*[@id="btnLoginModal"]').click()
time.sleep(1)
input1 = driver.find_element_by_xpath('//*[@id="username"]')
input1.clear()
input1.send_keys(username)
input2 = driver.find_element_by_xpath('//*[@id="password"]')
input2.clear()
input2.send_keys(password)
driver.find_element_by_xpath('//*[@id="btnLogin"]').click()

time.sleep(1)

driver.get(file1_url)
driver.get(file2_url)
driver.get(file3_url)