from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium import webdriver

class Window_Size_JS_Command ():
    def Chrome_Method(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/pages/practice")
        #driver.execute_script("window.location ='https://letskodeit.teachable.com/pages/practice';")#method to execute JS, window.location is the command to open pages.
        driver.implicitly_wait(3)

        # SCROLL DOWN, with JS method
        driver.execute_script("window.scrollBy(0, 655);") #takes 2 args, vertical & horizontal
        time.sleep(3)

        # SCROLL UP, with JS method
        driver.execute_script("window.scrollBy(0, - 655);")  # takes 2 args, vertical & horizontal, Negative to go up
        time.sleep(3)

        # SCROLL ELEMENT INTO VIEW, with JS method
        #Problem with this is that it will take it to the top, it my get hidden behind other element,so
        #it can be used, but then add an scroll up
        element = driver.find_element_by_id("mousehover") #first find the element
        driver.execute_script("arguments[0].scrollIntoView(true);" , element) # then, use the JS command to bring into view and specify the "element to be brought to view"
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, -150);")  #then scroll up a little.
        time.sleep(3)

        # SCROLL ELEMENT INTO VIEW, with NATIVE method
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, -1000);") # first scroll up a little.
        locationInfo= element.location_once_scrolled_into_view #the locationInfo variable with use the "element" and get it's location info and return it into locationInfo variable
        #location will be from TOP-LEFT
        print("Location: "+ str(locationInfo))
        time.sleep(3)



        driver.close()

# NOTE:
# IF LOOKING FOR THE WINDOW SIZE, YOU USE THE WINDOW MINIZED OR MAXIMIZED, IF WILL RETURN DIFF VALUES




Chromee = Window_Size_JS_Command()
Chromee.Chrome_Method()
