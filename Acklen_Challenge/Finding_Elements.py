from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


class AcklenAvenueChallenge():
    def Challenge(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.shino.de/parkcalc/")
        driver.implicitly_wait(5)  # have selenium wait for 10 secs before performing the next action.

        #Looking for the 1st dropdown
        ParkingLotDropdown = driver.find_element(By.ID, "ParkingLot")
        sel = Select(
            ParkingLotDropdown)
        sel.select_by_value("Economy")
        # sel.select_by_index("2")  # use the index property to find the option I want

        #Finding and filling the entry date & time and AM/PM radio btn
        EntryDate_Field = driver.find_element(By.ID, "StartingDate")
        EntryDate_Field.clear()
        EntryDate_Field.send_keys("6/30/2021")

        StartTime_Field = driver.find_element(By.ID, "StartingTime")
        StartTime_Field.clear()
        StartTime_Field.send_keys("12:00")

        PM_radiobtn = driver.find_element_by_xpath("//tbody/tr[2]/td[2]/input[4]")
        PM_radiobtn.click()

        # Finding and filling the leave date & time and AM/PM radio btn
        LeaveDate_Field = driver.find_element(By.ID, "LeavingDate")
        LeaveDate_Field.clear()
        LeaveDate_Field.send_keys("7/31/2021")

        LeaveTime_Field = driver.find_element(By.ID, "LeavingTime")

        LeaveTime_Field.clear()
        LeaveTime_Field.send_keys("15:00")

        AM_radiobtn = driver.find_element_by_xpath("//tbody/tr[3]/td[2]/input[3]")
        AM_radiobtn.click()
        time.sleep(10)

        #Clicking the Calculate btn to execute a basic happy path escenario.
        CalculateBtn = driver.find_element(By.XPATH, "//body/form[1]/input[2]")
        CalculateBtn.click()

        driver.quit()


Chlg = AcklenAvenueChallenge()
Chr.Challenge()
