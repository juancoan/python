#THIS EXAMPLE IS USING THE DRIVER EXPLICITLY MENTIONED ON THE CODE.

from selenium import webdriver #import selenium webdriver library
import os # import os library support

class Prueba_Chrome ():
    def Chrome_Method(self):
        DriverLocation = "C:\\Users\\Dell\\Desktop\\Python\\Code\\chromedriver\\chromedriver.exe" #specify path on a variable of the chromedriver
        os.environ["webdriver.chrome.driver"] = DriverLocation #asociate the location variable to the os.environ variable.
        driver = webdriver.Chrome(executable_path=DriverLocation) #associate the driver variable location to the driver instance
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.close()

Chromee = Prueba_Chrome()
Chromee.Chrome_Method()