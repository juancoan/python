"""
Links to check for the logging parameters and adding/removing info
https://docs.python.org/3/library/logging.html#logrecord-attributes
https://docs.python.org/3/library/time.html#time.strftime
"""

import logging
from selenium import webdriver


#METHOD TO SPECIFY THE FILE WHERE TO SAVE THE LOG INFO & LEVEL
#with the format variable I can change the format of the log, s = space, % is for info.
# time is represented as (asctime), also dateformat to adjust the way it is shown
#to show 24H clock, it will be to change %I to %H
logging.basicConfig(format= '%(asctime)s:, %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
logging.warning("Some Warning")
logging.info("Some Info")
logging.error("Some ERROR happened")

