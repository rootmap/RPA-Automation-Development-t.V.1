import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\driver\chromedriver_win32\chromedriver.exe")

driver.get("http://v4.nucleuspos.com/login")

print("Login page Title = ",driver.title)

username = driver.find_element_by_name("email")
print(username.is_displayed())
print(username.is_enabled())

password = driver.find_element_by_name("password")
print(password.is_displayed())
print(password.is_enabled())

username.send_keys("text@aol.com")
password.send_keys("123")

driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/section/div/div[2]/div/form/button").click()

time.sleep(10)

print("Logged In page Title = ",driver.title)

driver.close()