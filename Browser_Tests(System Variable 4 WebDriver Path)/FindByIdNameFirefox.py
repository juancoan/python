#THIS EXAMPLE IS USING THE DRIVER MENTIONED ON a SYSTEM VARIABLE, NOT ON THE CODE.

from selenium import webdriver #import selenium webdriver library
from selenium.webdriver.common.by import By #Import to use the BY on the find elements by

class Find_NameID ():
    def Firefox_Method(self):
        driver = webdriver.Firefox()
        driver.get("https://learn.letskodeit.com/p/practice")
        print("*#"*20)
        elementByID = driver.find_element_by_id("name")#trying to find element with id="name
        if elementByID is not None:
            print("I found it, element by ID")
        print("*#" * 20)
        elementByName = driver.find_element_by_name("cars")#trying to find element with name="cars
        if elementByName is not None:
            print("I found it, element by Name")
        print("*#" * 20)
        elementBy= driver.find_element(By.XPATH, "//div[@id='radio-btn-example']//label[3]")

        if elementBy is not None:
            print("Found it using Find_Element()")
        driver.close()
#associate the driver.find or driver.method to a variable to make comparisons, ifs, etc.

Chromee = Find_NameID()#Instanciando la clase
Chromee.Firefox_Method()#usando el metodo desde la instancia