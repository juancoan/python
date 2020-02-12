from traceback import print_stack
from selenium.webdriver.common.by import By
from Code.Utilities.Handy_Wrappers import HandyWrappers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicitWaitType():
    def __init__(self, driver):
        self.driver = driver #passing the driver as a param.
        self.HW = HandyWrappers(driver) #Calling and instanciating the handrywrappers class


    def waitForElement(self, Locator, LocatorType="id",
                       timeout=10, pollFrequency=1):
        element = None
        try:
            byType = self.HW.getByType(LocatorType)#creating a new variable to store the ByType from the getByType method on HW class
            print("Waiting for max ::", timeout , " seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 20, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, "stopFilter_stops-0")))
            print("Element appeared on he web page")
        except:
            print("Element did not appear on the web page")
            print_stack()
        return element


