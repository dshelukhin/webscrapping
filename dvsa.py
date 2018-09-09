from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

option = webdriver.ChromeOptions()
option.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=option)
driver.get('https://www.gov.uk/change-driving-test')

driver.find_element_by_xpath("//p[@id='get-started']/a[1]").click()
# driver.find_element_by_xpath("//*[@id='main']/section/a").click()

input1 = driver.find_element_by_xpath("//*[@id='driving-licence-number']")
input1.clear()
input1.send_keys("*DRIVING LICENSE NO*")
input2 = driver.find_element_by_xpath("//*[@id='application-reference-number']")
input2.clear()
input2.send_keys("*REF NO*")

driver.find_element_by_xpath("//*[@id='booking-login']").click()
driver.find_element_by_xpath("//*[@id='test-centre-change']").click()

input3 = driver.find_element_by_xpath("//*[@id='test-centres-input']")
input3.clear()
input3.send_keys("Hither Green")

driver.find_element_by_xpath("//*[@id='test-centres-submit']").click()
driver.find_element_by_xpath("//*[@id='centre-name-120']").click()

current_month = driver.find_element_by_xpath("//*[@id='slot-picker-form']/div[1]/div[1]/div[1]/span[@class='BookingCalendar-currentMonth']")
print("Current month:", current_month.text)
if current_month.text == "July":
    print("July available")
elif current_month.text == "June":
    print("July fully booked")
    driver.find_element_by_xpath("//*[@id='slot-picker-form']/div[1]/div[1]/div[1]/a[2]").click()
    time.sleep(5)
    driver.close()
else:
    print("July fully booked")
    time.sleep(5)
    driver.close()

# time.sleep(4)

# driver.close()