#THIS EXAMPLE IS USING THE DRIVER EXPLICITLY MENTIONED ON THE CODE.

from selenium import webdriver

class Prueba_Chrome ():
    def Chrome_Method(self):
        driver = webdriver.Chrome()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.close()

Chromee = Prueba_Chrome()
Chromee.Chrome_Method()