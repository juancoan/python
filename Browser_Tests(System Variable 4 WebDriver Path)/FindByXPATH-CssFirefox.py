#THIS EXAMPLE IS USING THE DRIVER MENTIONED ON a SYSTEM VARIABLE, NOT ON THE CODE.

from selenium import webdriver #import selenium webdriver library
from selenium.webdriver.common.by import By #Import to use the BY on the find elements by

class Find_XpathCss():
    def FF_Method(self):
        driver = webdriver.Firefox()
        driver.get("https://learn.letskodeit.com/p/practice")
        print("*#"*20)
        elementByXPATH = driver.find_elements_by_xpath("//legend[contains(text(),'Switch Tab Example')]")#trying to find element with xpath
        if elementByXPATH is not None:
            print("I found it, element by XPATH")
        print("*#" * 20)
        elementByXPATH2= driver.find_element(By.XPATH, "//legend[contains(text(),'Switch Tab Example')]")
        if elementByXPATH2 is not None:
            print("Found it using Find_Element(By.XPATH)")
        print("*#" * 20)
        elementByCSS = driver.find_element_by_css_selector("div:nth-of-type(2) > .left-align > fieldset > legend")
        if elementByCSS is not None:
            print("Found element by CSS")
        driver.close()
#associate the driver.find or driver.method to a variable to make comparisons, ifs, etc.

FF = Find_XpathCss()#Instanciando la clase
FF.FF_Method() #usando el metodo desde la instancia