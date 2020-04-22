from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver_win32\chromedriver.exe")
driver.get("http://indiangarden.bhuyianhost.com/login")

#wait some time here | due to url open will take some time
driver.implicitly_wait(10)

assert "AdminPanel | Log in" in driver.title

username = driver.find_element_by_name("email").send_keys("f.bhuyian@gmail.com")
password = driver.find_element_by_name("password").send_keys("111")
driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[3]/div[2]/button").click()
