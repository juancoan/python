from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BrowserInteractions():
    def Interactions(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")

        OpenTabElement = driver.find_element(By.ID, "opentab")
        Texto = OpenTabElement.text # to obtain the text on the element
        print("The text on the Open Tab button is: ", Texto)
        time.sleep(3)

        driver.quit()

Chr = BrowserInteractions()
Chr.Interactions()