from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BrowserInteractions():
    def Interactions(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://expedia.com")
        driver.implicitly_wait(5)

        #finding the flights tab & clicking
        FlightsTab = driver.find_element(By.XPATH, "//button[@id='tab-flight-tab-hp']")
        FlightsTab.click()

        # finding the departure field & clicking
        DepartingField = driver.find_element(By.ID, "flight-departing-hp-flight")
        DepartingField.click()
        time.sleep(3)

        #Seleting the date
        DateToDepart = driver.find_element_by_xpath("//button[contains(text(),'29')]//span[contains(text(),'March')]")
        DateToDepart.click()

        time.sleep(3)
        driver.quit()

Chromee = BrowserInteractions()
Chromee.Interactions()