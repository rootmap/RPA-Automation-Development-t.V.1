import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver_win32\chromedriver.exe")

driver.get("http://v4.nucleuspos.com/login")

print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/section/div/div[2]/div/form/button").submit()

print(driver.title)
print(driver.current_url)
print(driver.page_source)

time.sleep(5)

driver.close() #close current focus page
driver.quit() #close all page which is running by automation page
