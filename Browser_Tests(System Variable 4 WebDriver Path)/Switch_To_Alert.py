from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium import webdriver

class Switch_To_ALERT():
    def Chrome_Method(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/pages/practice")
        driver.implicitly_wait(3)

        #ALERT POPUP BTN
        driver.find_element(By.ID, "name").send_keys("JuanCo") # find the field to insert the name
        driver.find_element(By.ID, "alertbtn").click() # find the id for the ALERT btn
        time.sleep(3)

        alertPopUp = driver.switch_to.alert
        alertPopUp.accept() #this ACCEPT() method is like the CLICK() option, it is to click it and ACCEPT
        time.sleep(5)

        # CONFIRM POPUP BTN
        driver.find_element(By.ID, "name").send_keys("JuanCo")  # find the field to insert the name
        driver.find_element(By.ID, "confirmbtn").click()  # find the id for the ALERT btn
        time.sleep(3)

        # HERE YOU HAVE TO CHOOSE EITHER TO DISMISS OR ACCEPT, COMMENT 1 OF THE 2 TO TEST.
        alertPopUp2 = driver.switch_to.alert
        #alertPopUp2.accept()  # this ACCEPT() method is like the CLICK() option, it is to click it and ACCEPT
        alertPopUp2.dismiss()  # this DISMISS() method is like the CLICK() option, it is to click it and CANCEL
        time.sleep(3)

        driver.close()

#driver.quit() closes EVERYTHING
#driver.close() closes the CURRENT window with the focus.

Chromee = Switch_To_ALERT()
Chromee.Chrome_Method()

#windows are used with "handles" in selenium, a string