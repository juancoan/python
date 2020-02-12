#THIS EXAMPLE IS USING THE DRIVER MENTIONED ON a SYSTEM VARIABLE, NOT ON THE CODE.

from selenium import webdriver #importing selenium webdriver
import os

class PruebaFF(): #CLASE
    def FF_Method(self): #METODO
        driver = webdriver.Firefox()
        driver.get("http://www.letskodeit.com")
        driver.close()

FF = PruebaFF() #INSTANCIA
FF.FF_Method()#EJECUTO METODO
