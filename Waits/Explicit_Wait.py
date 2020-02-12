from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class BrowserInteractions():
    def Interactions(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
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
        wait = WebDriverWait(driver, 10, poll_frequency=1,
                            ignored_exceptions=[NoSuchElementException,
                                                ElementNotVisibleException,
                                                ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.ID, "stopFilter_stops-0")))
        element.click()

        time.sleep(3)
        driver.quit()

Chromee = BrowserInteractions()
Chromee.Interactions()

