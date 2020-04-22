import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\driver\chromedriver_win32\chromedriver.exe")

driver.get("http://nucleuspos.com") #first app open
print(driver.title)
driver.get("http://simpleretailpos.com") #second app open

time.sleep(5) #giving some time to excute the command for next url

print(driver.title)

driver.back() #now going back to nucleus site
time.sleep(5) #giving some time to excute the command for next url
print(driver.title)

driver.forward() #now going forward again to simpleretailpos site
time.sleep(5) #giving some time to excute the command for next url
print(driver.title)

driver.close()
