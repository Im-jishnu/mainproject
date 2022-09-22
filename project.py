from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver_win32 (1)\\chromedriver.exe")
driver.get("https://visatravelm.com/dummy-air-ticket/")
ww=driver.find_element(by=By.NAME,value="ticket-type-TYPE")
aa=Select(ww)
aa.select_by_visible_text("Dummy ticket for Visa Application — 699 INR")
driver.find_element(by=By.NAME,value="first-name").send_keys("jishnu")

