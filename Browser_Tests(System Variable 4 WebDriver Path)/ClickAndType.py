from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BrowserInteractions():
    def Interactions(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.implicitly_wait(5) #have selenium wait for 10 secs before performing the next action.
        # It will be applied to ALL elements

        Login_Link = driver.find_element(By.XPATH,"//a[contains(@href,'/sign_in')]")
        Login_Link.click()

        Email_Field = driver.find_element(By.ID, "user_email")
        Email_Field.click()
        Email_Field.send_keys("wiver@hotmail.com")# using SEND_KEYS() method to write

        Pass_Field = driver.find_element(By.ID, "user_password")
        Pass_Field.send_keys("111111")
        time.sleep(5) #method to put a wait of X secs

        Email_Field.clear()# using CLEAR() method to cler content
        Pass_Field.clear()
        time.sleep(5)  # method to put a wait of X secs

        Email_Field.send_keys("")# using SEND_KEYS() method to write
        Pass_Field.send_keys("")

        driver.quit()


Chr = BrowserInteractions()
Chr.Interactions()