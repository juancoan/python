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
        #driver.get("https://letskodeit.teachable.com/pages/practice")
        driver.execute_script("window.location ='https://letskodeit.teachable.com/pages/practice';")#method to execute JS, window.location is the command to open pages.
        driver.implicitly_wait(3)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")

        print("The height of the window is: " , height , " px")
        print("The width of the window is: " , width , " px")
        driver.close()

# NOTE:
# IF LOOKING FOR THE WINDOW SIZE, YOU USE THE WINDOW MINIZED OR MAXIMIZED, IF WILL RETURN DIFF VALUES




Chromee = Window_Size_JS_Command()
Chromee.Chrome_Method()
