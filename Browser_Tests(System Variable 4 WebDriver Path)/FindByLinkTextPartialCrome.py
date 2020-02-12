#THIS EXAMPLE IS USING THE DRIVER MENTIONED ON a SYSTEM VARIABLE, NOT ON THE CODE.

from selenium import webdriver #import selenium webdriver library
from selenium.webdriver.common.by import By #Import to use the BY on the find elements by

class Find_Partial_Link_Text():
    def Chrome_Method(self):
        driver = webdriver.Chrome()
        driver.get("https://learn.letskodeit.com/p/practice")
        print("*#"*20)
        elementByXPATH = driver.find_element_by_link_text("Login")#trying to find element with xpath
        if elementByXPATH is not None:
            print("I found it, element by Link Text")
        print("*#" * 20)
        elementByXPATH2= driver.find_element_by_partial_link_text("Pract")
        if elementByXPATH2 is not None:
            print("Found it using Partial Link Text")
        print("*#" * 20)
        driver.close()
#associate the driver.find or driver.method to a variable to make comparisons, ifs, etc.

Chromee = Find_Partial_Link_Text()#Instanciando la clase
Chromee.Chrome_Method() #usando el metodo desde la instancia