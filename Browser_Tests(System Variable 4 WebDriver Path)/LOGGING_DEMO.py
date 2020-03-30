"""
Logging levels:
DEBUG -> To search for errors, issues, bugs, detailed info
INFO -> Confirmation of things working as expected
WARNING -> Something unexpected happened, some problem may happen in the future
ERROR -> Some error happened
CRITICAL -> Something really bad happened.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
import logging
from selenium import webdriver

# class Logging():
#     def Chrome_Method(self):
#         driver = webdriver.Chrome()
#         driver.maximize_window()
#         driver.get("https://jqueryui.com/slider/")
#         driver.implicitly_wait(3)

#METHOD TO SPECIFY THE FILE WHERE TO SAVE THE LOG INFO & LEVEL
logging.basicConfig(filename="test.log",level=logging.DEBUG)
logging.warning("Some Warning")
logging.info("Some Info")
logging.error("Some ERROR happened")






# Chromee = Logging()
# Chromee.Chrome_Method()