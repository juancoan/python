from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


class Computer_DB():
    def Delete_Entry(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://computer-database.herokuapp.com/computers")
        driver.implicitly_wait(5)

        ToFind_Link = driver.find_element(By.XPATH,"//a[contains(text(),'ACE')]")
        ToFind_Link.click()
        time.sleep(3)

        Delete_Btn = driver.find_element(By.XPATH, "//input[@class = 'btn danger']")
        Delete_Btn.click()
        time.sleep(5)
        driver.quit()


Entry = Computer_DB()
Entry.Delete_Entry()