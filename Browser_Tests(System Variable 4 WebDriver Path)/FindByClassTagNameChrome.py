#THIS EXAMPLE IS USING THE DRIVER MENTIONED ON a SYSTEM VARIABLE, NOT ON THE CODE.

from selenium import webdriver #import selenium webdriver library
import os # import os library support

class FindyByClassTagName_Chrome():
    def Chrome_Method(self):
        driver = webdriver.Chrome() #associate the driver variable location to the driver instance
        driver.get("https://learn.letskodeit.com/p/practice")
        titulo = driver.title

        elementByClassName = driver.find_element_by_class_name("displayed-class")
        elementByClassName.send_keys("JuanCo test")  # to write/send data on the field
        if elementByClassName is not None:
            print("Found element by class name")

        elementByTagName = driver.find_element_by_tag_name("h1")
        textOnElement = elementByTagName.text #associate to a variable the text property of the webelement found
        if elementByTagName is not None:
            print("Found element by tag name -> ", textOnElement)

        print("Titulo de la pagina: " + titulo)
        driver.maximize_window()
        driver.close()

Chromee = FindyByClassTagName_Chrome()
Chromee.Chrome_Method()