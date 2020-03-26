from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium import webdriver

class MouseOver():
    def Chrome_Method(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/pages/practice")
        driver.implicitly_wait(3)

        driver.execute_script("window.scrollBy(0, 800);") #scrolling down
        time.sleep(3)
        MouseOverElement = driver.find_element(By.ID, "mousehover") #finding the MouseOver button
        itemToClickLocator = ".//div[@class='mouse-hover-content']//a[text()='Top']"#locating the 'Top' option
        #itemToClickLocator = ".//div[@class='mouse-hover-content']//a[text()='Reload']"#locating the 'Reload' option

        try:
            actions = ActionChains(driver) #to enable the ActionChains through driver(instance)
            actions.move_to_element(MouseOverElement).perform() #method to JUST move to the Mouse Over button, ALWAYS use perform
            print("Mouse hovered over element.") # to show it hovered over
            time.sleep(5)

            #Once the "Mouse Hover" button has the mouse over and the menu pops up then locate the option I want
            topLink = driver.find_element(By.XPATH, itemToClickLocator)  # locating element on the mouse over popup
            actions.move_to_element(topLink).click().perform()# to JUST move to the option I want and click it.
            print("Item clicked.")
        except:
            print("Mouse Hover failed element.")

        time.sleep(3)

Chromee = MouseOver()
Chromee.Chrome_Method()
