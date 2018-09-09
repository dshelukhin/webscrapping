import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

username = '*'
password = '*'

option = webdriver.ChromeOptions()
# option.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=option)
driver.get('https://products.markit.com/home/index.jsp')

input1 = driver.find_element_by_xpath("//*[@id='username']")
input1.clear()
input1.send_keys(username)
input2 = driver.find_element_by_xpath("//*[@id='password']")
input2.clear()
input2.send_keys(password)
driver.find_element_by_xpath("//*[@id='submit']").click()

time.sleep(10)
driver.get('https://products.markit.com/home/index.jsp#INDICES.HOME.home')

file_url = 'https://products.markit.com/indices/data/DataOutputExcel.xls?queryID=DWmembers&isd_index=I12100042&family=ib_EUR&app=excel&date=07%2E09%2E2018&fixing=EU_EOD&Level0=EUR&return=TRi&key=ISIN&bondtype=1'

time.sleep(5)

cookies = driver.get_cookies()
s = requests.Session()
for cookie in cookies:
    s.cookies.set(cookie['name'], cookie['value'])
r = s.get(file_url)
r.raise_for_status()
print(r.url)
print(r.status_code)

file = open('QW5A.xls', 'wb')
file.write(r.content)