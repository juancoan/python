from selenium import webdriver
from selenium.webdriver.common.by import By
import time


"""
Created by Juan Antonio Cordoba
Class for updating a new computer entry.
"""


class Computer_DB():
    def Update_Entry(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://computer-database.herokuapp.com/computers")
        driver.implicitly_wait(5)

        ToFind_Link = driver.find_element(By.XPATH,"//a[contains(text(),'ASCI Purple')]")
        ToFind_Link.click()
        time.sleep(3)

        DiscDate_Field = driver.find_element(By.ID, "discontinued")
        DiscDate_Field.send_keys("2030-12-01")
        time.sleep(3)

        Delete_Btn = driver.find_element(By.XPATH, "//input[@class = 'btn primary']")
        Delete_Btn.click()
        time.sleep(5)
        driver.quit()


Entry = Computer_DB()
Entry.Update_Entry()