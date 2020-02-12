#THIS EXAMPLE IS USING THE DRIVER EXPLICITLY MENTIONED ON THE CODE.

from selenium import webdriver

class Prueba_Chrome ():
    def Chrome_Method(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\juan.cordoba\\Desktop\\Python-Automation\\Code\\chromedriver\\chromedriver.exe") #specify path
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.close()

Chromee = Prueba_Chrome()
Chromee.Chrome_Method()