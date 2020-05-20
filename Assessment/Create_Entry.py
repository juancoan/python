from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


"""
Created by Juan Antonio Cordoba
Class for creating a new computer entry.
"""

class Computer_DB():
    def Create_Entry(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://computer-database.herokuapp.com/computers")
        driver.implicitly_wait(5)

        Create_Link = driver.find_element(By.ID,"add")
        Create_Link.click()
        time.sleep(3)

        Computer_Field = driver.find_element(By.ID, "name")
        Computer_Field.click()
        Computer_Field.send_keys("JuanCo")

        IntDate_Field = driver.find_element(By.ID, "introduced")
        IntDate_Field.send_keys("2020-05-22")
        time.sleep(3)

        DiscDate_Field = driver.find_element(By.ID, "discontinued")
        DiscDate_Field.send_keys("2001-12-01")
        time.sleep(3)

        Company_DropDown = driver.find_element_by_id("company")
        sel = Select(Company_DropDown)
        sel.select_by_value("28")
        time.sleep(3)

        Create_Btn = driver.find_element(By.XPATH, "//input[@class='btn primary']")
        Create_Btn.click()
        time.sleep(5)
        driver.quit()


Entry = Computer_DB()
Entry.Create_Entry()