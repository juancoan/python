from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BrowserInteractions():
    def Interactions(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.implicitly_wait(5)

        #To find the Hide/Show field and see if it is displayed
        HideShowField = driver.find_element_by_id("displayed-text")
        FieldState = HideShowField.is_displayed() # is it shown on the page
        print("Hide/Show field is displayed? ", FieldState)
        time.sleep(3)

        #To find and click the HIDE button
        HideBtn = driver.find_element_by_id("hide-textbox")
        HideBtn.click()
        time.sleep(3)

        # To find the if the  Hide/Show field is displayed after clicking HIDE btn
        FieldState = HideShowField.is_displayed() # is it shown on the page
        print("Hide/Show field is displayed after clicking the Hide btn? ", FieldState)
        time.sleep(3)

        # To find and click the SHOW button
        HideBtn = driver.find_element_by_id("show-textbox")
        HideBtn.click()
        time.sleep(3)

        # To find the if the  Hide/Show field is displayed after clicking SHOW btn
        FieldState = HideShowField.is_displayed()  # is it shown on the page
        print("Hide/Show field is displayed after clicking the Show btn? ", FieldState)
        time.sleep(3)


Chr = BrowserInteractions()
Chr.Interactions()
