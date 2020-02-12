#THIS EXAMPLE IS USING THE DRIVER EXPLICITLY MENTIONED ON THE CODE.

from selenium import webdriver #import selenium webdriver library
import os # import os library support

class Prueba_IE():
    def IE_Method(self):
        DriverLocation = "C:\\Users\\juan.cordoba\\Desktop\\Python-Automation\\Code\\IEDriver\\IEDriverServer.exe" #specify path on a variable of the chromedriver
        os.environ["webdriver.ie.driver"] = DriverLocation #asociate the location variable to the os.environ variable.
        driver = webdriver.Ie(executable_path=DriverLocation) #associate the driver variable location to the driver instance
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.close()

IE = Prueba_IE()
IE.IE_Method()



