from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium import webdriver

class Drag_And_Drop():
    def Chrome_Method(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://jqueryui.com/droppable/")
        driver.implicitly_wait(3)

        driver.switch_to.frame(0)# switching to the frame because those items are on the IFRAME!
        time.sleep(3)
        fromElement = driver.find_element(By.ID, "draggable") #finding the item that is to be dragged
        toElement = driver.find_element(By.ID, "droppable") #finding the place where to drop
        time.sleep(3)

        try: #METHOD #1
            actions = ActionChains(driver) #to enable the ActionChains through driver(instance)
            actions.drag_and_drop(fromElement, toElement).perform() #method to DRAG&DROP, uses 2 params
            print("Drag and Drop element SUCCESSFUL.") # to show it was dragged and dropped fine.
            time.sleep(5)

            #METHOD #2 - SEPARATE ACTIONS - UNCOMMENT CODE
            # actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
            # print("Drag and Drop element SUCCESSFUL.")  # to show it was dragged and dropped fine.
            # time.sleep(5)
            #use to specify to first click & hold 1st element then move to the 2nd element, then release
            #perform() is ALWAYS used/written


        except:
            print("Drag and Drop element FAILED")

        time.sleep(3)

Chromee = Drag_And_Drop()
Chromee.Chrome_Method()
