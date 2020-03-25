from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium import webdriver

class Switch_To_iFRAME():
    def Chrome_Method(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/pages/practice")
        driver.implicitly_wait(3)
        driver.execute_script("window.scrollBy(0, 1000);")  # takes 2 args, SCROLL down

        #TO AVOID ISSUES, WHEN USING EITHER OF THE 3 SEARCH OPTIONS
        #(ID, NAME, NUMBERS), PLS, COMMENT THE OTHERS


        #Switch to the frame using ID
        #driver.switch_to.frame("courses-iframe")# this is the command to switch to the IFRAME, with id.

        # Switch to the frame using NAME
        #driver.switch_to.frame("iframe-name")  # this is the command to switch to the IFRAME, with name.

        # Switch to the frame using NUMBERS
        driver.switch_to.frame(0)  # this is the command to switch to the IFRAME, with number, like the index on the list.

        time.sleep(3)
        #Search course
        searchBox = driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("Python")
        time.sleep(3)

        #Switch back to the parent frame
        driver.switch_to.default_content()  # switching back to the PARENT IFRAME
        driver.execute_script("window.scrollBy(0, -1000);")  # takes 2 args, SCROLL UP
        time.sleep(5)

        #Type something on the field on the PARENT frame
        driver.find_element_by_id("name").send_keys("SUCCESS.")
        time.sleep(5)






#driver.quit() closes EVERYTHING
#driver.close() closes the CURRENT window with the focus.

Chromee = Switch_To_iFRAME()
Chromee.Chrome_Method()

#windows are used with "handles" in selenium, a string