from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BrowserInteractions():
    def Interactions(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")

        OpenTabElement = driver.find_elements(By.XPATH, "//legend[contains(text(),'Example')]")

        Testo = OpenTabElement.copy()
        Quantity = len(OpenTabElement) # to obtain the text on the element
        print(Testo)
        print("Number of Instances. ", Quantity)
        time.sleep(3)
        driver.quit()

        Word2Find = "Example"
        for words in OpenTabElement:
            Splitted = words.split()



Chr = BrowserInteractions()
Chr.Interactions()