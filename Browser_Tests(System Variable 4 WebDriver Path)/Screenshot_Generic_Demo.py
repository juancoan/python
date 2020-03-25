from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium import webdriver

class Screenshots ():
    def Chrome_Method(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/")
        driver.implicitly_wait(3)

        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "user_email").send_keys("juansito@juanco.com")
        driver.find_element(By.ID, "user_password").send_keys("holis")
        driver.find_element(By.NAME, "commit").click()
        self.takeScreenshotGeneric(driver) #invoking the take screenshot generic method, driver as parameter


    #pretend as if this method was at another class.
    def takeScreenshotGeneric(self, driver):
        """
        Takes screenshot of the current open page
        :param driver:
        :return:
        """
        fileName = str(round(time.time()*1000))+ ".png" #variable to hold the filename separately (random chars)
        screenshotDirectory = "C:/Users/DELL/Desktop/Python/Code/Screenshots/"#variable to hold the location separately
        FullFileName = screenshotDirectory+fileName #variable to hold the filename +folder, full path

        try: #Use a try/except block in case the folder is present/valid but an error shows and it not a folder error
            driver.save_screenshot(FullFileName)
            print("SCREENSHOT TAKEN. Saved on: " + FullFileName)
        except NotADirectoryError:
            print("NOT a directory error, please check.")
            driver.close()

Chromee = Screenshots()
Chromee.Chrome_Method()
