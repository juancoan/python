from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BrowserInteractions():
    def Interactions(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.google.com")
        driver.implicitly_wait(5) #have selenium wait for 10 secs before performing the next action.
        # It will be applied to ALL elements

        Element1 = driver.find_element_by_name("iflsig")
       # Element1.send_keys("JuanCo")
        Element1_State = Element1.is_enabled()
        print("State of the element. Is it enabled: --> ", Element1_State)

        Element2 = driver.find_element_by_name("q")
        # Element2.send_keys("JuanCo")
        Element2_State = Element2.is_enabled()
        print("State of the element. Is it enabled: --> ", Element2_State)


Chr = BrowserInteractions()
Chr.Interactions()