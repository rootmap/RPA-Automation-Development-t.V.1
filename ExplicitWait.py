import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver_win32\chromedriver.exe")

driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://www.expedia.com/")
# driver.find_element_by_id("tab-flight-tab-hp").click()
driver.find_element(By.ID, "tab-flight-tab-hp").click()  # Flights Button Clicked

time.sleep(2)  # from python

driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")  # orgin #input text field by ID
time.sleep(2)  # from python
driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")  # destination #input text field by ID
time.sleep(2)  # from python

driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys(
    "05/29/2020")  # departute date #input text field by ID
time.sleep(2)  # from python

driver.find_element(By.ID, "flight-returning-hp-flight").click()
driver.find_element(By.ID, "flight-returning-hp-flight").clear()
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("06/17/2020")  # returning #input text field by ID
time.sleep(2)  # from python

driver.find_element(By.XPATH, "//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()

# explicit Wait statements
wait = WebDriverWait(driver, 10)  #
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stopFilter_stops-0']")))

element.click()

time.sleep(3)

driver.quit()
