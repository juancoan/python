from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BrowserInteractions():
    def Interactions(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.implicitly_wait(5) #have selenium wait for 10 secs before performing the next action.
        # It will be applied to ALL elements

        Element1 = driver.find_element_by_id("bmwradio")
        Element1.click()
        time.sleep(5)

        Element2 = driver.find_element_by_xpath("benzradio")
        Element2.click()
        time.sleep(5)

        Element3 = driver.find_element_by_id("hondaradio")
        Element3.click()
        time.sleep(5)

        Element4 = driver.find_element_by_id("bmwcheck")
        Element4.click()
        time.sleep(5)

        Element5 = driver.find_element_by_id("benzcheck")
        Element5.click()
        time.sleep(5)

        Element6 = driver.find_element_by_id("hondacheck")
        Element6.click()
        time.sleep(5)

        print("Is BMW radio button selected? ", Element1.is_selected())
        print("Is Honda check box displayed? ", Element6.is_displayed())

Chr = BrowserInteractions()
Chr.Interactions()