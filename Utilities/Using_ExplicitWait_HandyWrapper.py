from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import *
from Code.Utilities.Explicit_Wait_HandyWrapper import ExplicitWaitType

class BrowserInteractions():
    def Interactions(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        wait = ExplicitWaitType(driver)
        driver.get("https://expedia.com")
        driver.implicitly_wait(2)

        #Filling the flight tab form
        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
        driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("02/24/2020")

        returnDate = driver.find_element(By.ID, "flight-returning-hp-flight")
        returnDate.click()
        time.sleep(1)
        # Used JavaScript to clear the field
        driver.execute_script("arguments[0].value='';", returnDate)
        time.sleep(1)
        returnDate.send_keys("03/24/2020")
        driver.find_element(By.XPATH, "//form[@id='gcw-flights-form-hp-flight']//button[@class='btn-primary btn-action gcw-submit']").click()

        #EXPLICIT WAIT DECLARATION SINTAX
        element = wait.waitForElement("stopFilter_stops-0")
        element.click()

        time.sleep(3)
        driver.quit()

Chromee = BrowserInteractions()
Chromee.Interactions()

