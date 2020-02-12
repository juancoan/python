from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BrowserInteractions():
    def Interactions(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.implicitly_wait(5) #have selenium wait for 10 secs before performing the next action.
        # It will be applied to ALL elements

        RadioBtnLIST = driver.find_elements(By.XPATH, "//input[contains(@type, 'radio') and contains(@name, 'cars')]")
        #with this xpath using contains, it will show the 3 radio buttons.
        sizeOfList = len(RadioBtnLIST)# finding out how many items show up
        print("Size of the located radio button list: ", sizeOfList)

        for radioBtn in RadioBtnLIST: #iterating over the list that was found
            isClicked = radioBtn.is_selected() #using the iterating variable to check on each on if it is clicked
            BtnName =  radioBtn.get_attribute("value")#with this I can get an attribute of the element like name, value, etc
            print("Is radio button clicked? ", isClicked)

            if not isClicked: #if it is not clicked, then click it.
                radioBtn.click()
                print("Clicked ", BtnName, " radio button.")

                time.sleep(3)

Chr = BrowserInteractions()
Chr.Interactions()