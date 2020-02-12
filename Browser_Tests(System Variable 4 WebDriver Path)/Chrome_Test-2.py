#THIS EXAMPLE IS USING THE DRIVER MENTIONED ON a SYSTEM VARIABLE, NOT ON THE CODE.

from selenium import webdriver #import selenium webdriver library
import os # import os library support

class Prueba_Chrome ():
    def Chrome_Method(self):
        driver = webdriver.Chrome() #associate the driver variable location to the driver instance
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.close()

Chromee = Prueba_Chrome()
Chromee.Chrome_Method()