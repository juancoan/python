from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium import webdriver

class Switch_To_Window():
    def Chrome_Method(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/pages/practice")
        driver.implicitly_wait(3)

        #Find parent handle -> Main Window
        parentHandle = driver.current_window_handle #provide info of the current handle(parent)
        print("Parent Handle: ", parentHandle)


        #Find open window button and click it
        driver.find_element_by_id("openwindow").click()
        time.sleep(3)


        #Find all handles, there should be two handles after clicking open window button
        allHandles = driver.window_handles # will save all the handles. (parent and child)


        #Switch to window and search course
        #loop over the handles
        for handle in allHandles:
            print("Handle: " + handle)
            if handle not in parentHandle: # use if conditional to ask if I am on the NOT parent window
                driver.switch_to.window(handle) # if I am not on the parent handle, then switch to it (handle)
                print("Yeeeey!!!, I am on the OTHER window, not parent one.")
                searchBox = driver.find_element(By.ID, "search-courses")
                searchBox.send_keys("Python")
                time.sleep(3)
                driver.close()
                break # break out of the loop

        #Switch back to the parent handle
        driver.switch_to.window(parentHandle)  # switching back to the PARENT handle
        print("Yeeeey!!!, I am on the PARENT window, now.")
        driver.find_element_by_id("name").send_keys("Back on the Parent handle.")
        time.sleep(10)
#driver.quit() closes EVERYTHING
#driver.close() closes the CURRENT window with the focus.

Chromee = Switch_To_Window()
Chromee.Chrome_Method()

#windows are used with "handles" in selenium, a string