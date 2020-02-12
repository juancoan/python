from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BrowserInteractions():
    def Interactions(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com")
        driver.implicitly_wait(5)

        loginLink = driver.find_element(By.XPATH, "//div[@id = 'navbar']//a[@href='/sign_in']")
        loginLink.click()

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test")
        time.sleep(3)

Chromee = BrowserInteractions()
Chromee.Interactions()
