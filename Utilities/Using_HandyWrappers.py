from selenium import webdriver
from selenium.webdriver.common.by import By
from Code.Utilities.Handy_Wrappers import HandyWrappers #Import this class to call it's functionality
import time

class UsingWrappers():

    def Test_Wrappers(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        HW = HandyWrappers(driver)  # Instanciating the Handyrappers class and sending 'driver' param, define up
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.implicitly_wait(5)

        #Associating the 'textfield' variable to the method to extract the text
        #HW is the instance and getElement method to use the parameters and locate the element from the Handy_wrappers class
        #In this case name is the value of the attribute ID @id=name"
        #First find the element by id
        textfield1 = HW.getElement("name")#method expects locator, locator name, especified on the other class Handy_Wrappers
        textfield1.send_keys("Test")
        time.sleep(2)
        #then finding the same element by XPATH and clearing it
        textfield2 = HW.getElement("//input[@id='name']", LocatorType="xpath")
        textfield2.clear()
        time.sleep(3)

        #calling the instance of the Handy_wrappers class and using the method
        # Using the parameters locator, bytype
        textfield3 = HW.isElementPresent("name1", By.ID)
        print(textfield3)
        time.sleep(3)

        # calling the instance of the Handy_wrappers class and using the method
        textfield4 = HW.elementsPresenceCheck("//input[@id='name']", By.XPATH)
        print(textfield4)
        time.sleep(3)

Chromee = UsingWrappers()
Chromee.Test_Wrappers()

