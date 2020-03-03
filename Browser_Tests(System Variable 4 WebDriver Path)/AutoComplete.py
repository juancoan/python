from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Autocomplete():

    def test2(self):
        baseUrl = "http://www.southwest.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Send Partial Data
        cityField = driver.find_element_by_id("LandingAirBookingSearchForm_originationAirportCode")
        cityField.send_keys("New York")
        time.sleep(3)
        # Find the item and click
        itemToSelect = driver.find_element_by_xpath("//input[contains(text(),'LGA')]")
        itemToSelect.click()

        # time.sleep(3)
        # driver.quit()

ff = Autocomplete()
ff.test2()