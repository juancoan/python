from selenium import webdriver
from selenium.webdriver.common.by import By
import time

baseURL = 'https://www.redbus.in/'
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(baseURL)

startlocation = driver.find_element(By.ID, "src")
startlocation.send_keys('Pun')

time.sleep(2)
selectloc = driver.find_element(By.XPATH, "//ul[@class='autoFill']//li[contains(text(),'Wagholi')]")
selectloc.click()