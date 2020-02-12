from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BrowserInteractions():
    def Interactions(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com")
        driver.implicitly_wait(5)

        #Code for loging into the website
        driver.find_element(By.LINK_TEXT, "Login").click()
        email = driver.find_element(By.ID, "user_email")
        email.send_keys("test@email.com")
        password = driver.find_element(By.ID, "user_password")
        password.send_keys("abc123")
        driver.find_element(By.NAME, "commit").click()

        #Code for searching courses
        searchBox = driver.find_element(By.ID,"search-courses")
        #searchBox.send_keys("Javascript")

        driver.find_element(By.XPATH, "//a[@href = '/courses']").click()
        time.sleep(3)
        #Code for selecting the course, use {0}, {1} to replace it with the variable.format methode
        #_course variable used to store the dynamic xpath, with the {0}
        _course = "//div[contains(@class,'course-listing-title') and contains (text(), '{0}')]"
        #_courseLocator variable used to assoaicate it to the variable.format(text to//div[contains(@class,'course-listing-title') and contains(text(), '{0}')] be located)
        _courseLocator = _course.format("JavaScript for beginners")

        courseName = driver.find_element(By.XPATH, _courseLocator)
        courseName.click()
        time.sleep(3)

Chromee = BrowserInteractions()
Chromee.Interactions()


