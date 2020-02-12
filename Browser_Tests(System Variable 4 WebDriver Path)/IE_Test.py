#THIS EXAMPLE IS USING THE DRIVER MENTIONED ON a SYSTEM VARIABLE, NOT ON THE CODE.

from selenium import webdriver #import selenium webdriver library
import os # import os library support

class Prueba_IE():
    def IE_Method(self):
        driver = webdriver.Ie()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.close()

IE = Prueba_IE()
IE.IE_Method()



