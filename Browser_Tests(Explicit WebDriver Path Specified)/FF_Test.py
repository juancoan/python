#THIS EXAMPLE IS USING THE DRIVER EXPLICITLY MENTIONED ON THE CODE.

from selenium import webdriver #importing selenium webdriver
import os

class PruebaFF(): #CLASE
    def FF_Method(self): #METODO
        #location of the FF driver & starting the instance. Windows path uses double backslash and extension, mac does not
        #el nombre driver.XYZ es el nombre de la instancia del webdriver de FF
        driver = webdriver.Firefox(executable_path="C:\\Users\\juan.cordoba\\Desktop\\Python-Automation\\Code\\geckodriver\\geckodriver.exe")
        driver.get("http://www.letskodeit.com")
        driver.close()

FF = PruebaFF() #INSTANCIA
FF.FF_Method()#EJECUTO METODO
