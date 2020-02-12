#THIS EXAMPLE IS USING THE DRIVER MENTIONED ON a SYSTEM VARIABLE, NOT ON THE CODE.

from selenium import webdriver #import selenium webdriver library
import os # import os library support
from selenium.webdriver.common.by import By


class ListOfElements_Firefox ():
    def FF_Method(self):
        driver = webdriver.Firefox() #associate the driver variable location to the driver instance
        driver.get("https://learn.letskodeit.com/p/practice")

        ListElementsByClassName = driver.find_elements_by_class_name("inputs")  # locating all the elements that have the class inputs
        Cantidad = len(ListElementsByClassName)  # len will tell me the amount on a list.
        if ListElementsByClassName is not None:
            print("Found ", Cantidad, " elements of the Inputs class.")


        ListElementsByTagName = driver.find_elements(By.TAG_NAME, "div")  # locating all the elements that have the tag div
        Cantidad2 = len(ListElementsByTagName)  # len will tell me the amount on a list.
        if ListElementsByTagName is not None:
            print("Found ", Cantidad2, " elements of the Div tag.")

        driver.close()


Chromee = ListOfElements_Firefox()
Chromee.FF_Method()