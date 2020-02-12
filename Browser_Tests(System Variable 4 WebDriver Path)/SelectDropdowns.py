from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select # THIS IS FOR THE DROPDOWNS WITH SELECT TAG

class BrowserInteractions():
    def Interactions(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.implicitly_wait(5)

        Dropdown = driver.find_element_by_id("carselect") #Finding the dropdown element by ID
        sel = Select(Dropdown) # Selecting by using the SELECT class referencing the initial instance variable
        sel.select_by_value("benz") # use the value property to find the option I want
        time.sleep(3)

        sel.select_by_index("2") # use the index property to find the option I want
        time.sleep(3)

        sel.select_by_visible_text("BMW") # use the visible text property to find the option I want
        time.sleep(3)

        sel.select_by_index(1)  # use the index property WITHOUT QUOTES to find the option I want
        time.sleep(3)


Chr = BrowserInteractions()
Chr.Interactions()