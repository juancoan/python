from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium import webdriver

class JS_Scripts ():
    def Chrome_Method(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        #driver.get("https://letskodeit.teachable.com/pages/practice")
        driver.execute_script("window.location ='https://letskodeit.teachable.com/pages/practice';")#method to execute JS, window.location is the command to open pages.
        driver.implicitly_wait(3)

        #element = driver.find_element(By.ID, "name")
        #using return statement because we are retuning something
        element = driver.execute_script("return document.getElementById('name')") #using JS command to find the element by ID
        element.send_keys("Test")
        time.sleep(3)

        driver.close()

Chromee = JS_Scripts()
Chromee.Chrome_Method()
