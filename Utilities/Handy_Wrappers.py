from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class HandyWrappers():
    def __init__(self, driver):
        self.driver = driver #associate the driver to the local driver variable, initialize it

    #By which type you want to find the element, method
    #it should take as argument the type of locator.
    def getByType(self, LocatorType):
        LocatorType = LocatorType.lower() #to put everything on lower case, compare and return the correct way to write it
        if LocatorType == "id":
            return By.ID
        elif LocatorType == "name":
            return By.NAME
        elif LocatorType == "xpath":
            return By.XPATH
        elif LocatorType == "css":
            return By.CSS_SELECTOR
        elif LocatorType == "classname":
            return By.CLASS_NAME
        elif LocatorType == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type not supported. ")
        return False
        # the above validation  is to put everything on lower case.

    #Method to get the element, by Locator and LocatorType, based on the above method ie By.XPATH, "LOCATOR"
    def getElement(self, Locator, LocatorType="id"): #method to get the element, then perform actions
        element = None #initializing it to none
        try:
            LocatorType = LocatorType.lower()
            byType = self.getByType(LocatorType) #assign it to the byType variable,use the get method to apply it from the parameter  and use it on the statement below
            element = self.driver.find_element(byType, Locator) #build the driver.find statement with the generic format
            print("Element found. ")
        except:
            print("Element NOT found. ")
        return element

    #method to see if the element is present
    def isElementPresent(self, Locator, byType):
        try:
            element = self.driver.find_element(byType, Locator)
            if element is not None:
                print("Element found. ")
                return True # associate to a variable to show result on console
            else:
                return False  # associate to a variable to show result on console
        except:
            print("Element NOT found. ")
            return False  # associate to a variable to show result on console
    #method to see if the are elements present 1 or more than 1
    def elementsPresenceCheck(self, Locator, byType):
        try:
            elementList = self.driver.find_elements(byType, Locator)
            if len(elementList) > 0:
                print("Elements found. ", len(elementList))
                return True  # associate to a variable to show result on console
            else:
                print("NONE found. ", len(elementList))
                return False  # associate to a variable to show result on console
        except:
            print("Element NOT found. ", len(elementList))
            return False  # associate to a variable to show result on console
