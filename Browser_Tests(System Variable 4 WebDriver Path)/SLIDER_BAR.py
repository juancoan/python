from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium import webdriver

class Slider_Bar():
    def Chrome_Method(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://jqueryui.com/slider/")
        driver.implicitly_wait(3)

        driver.switch_to.frame(0)# switching to the frame because those items are on the IFRAME!

        sliderElement = driver.find_element(By.XPATH, "//div[@id='slider']//span")
        time.sleep(3)

        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(sliderElement,142, 0).perform() #ALWAYS INCLUDE PERFORM
            # method for dragging the bar, in this case we use the X axis to drag it to the left or right,
            # and use 0 on the Y axis. pixels is used on the values.
            print("Sliding Element SUCCESSFUL")
            time.sleep(3)
        except:
            print("Sliding Element FAILED")

        time.sleep(3)

Chromee = Slider_Bar()
Chromee.Chrome_Method()
