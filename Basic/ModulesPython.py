# Built-in functions on python
# https://docs.python.org/3/library/

"""
1st way to import the module on another package, it can load all the file within the package
import External_Module.Car as Car
this will import the module 'Car' that it resides on the External_Module pkge.
the 'as' keyword is to set an alias.

2nd way - BEST WAY -
from External_Module.Car import info
This will import just the info method/functionality
When you call it on the method, it has to be info(make, model)
"""
from External_Module import Car #Correct way to import the module from another package, directly

import math #Case 1.
from math import sqrt #Case 2. calling the sqrt part of Math module directly.
#this will import all the 'MATH' modules. Unless you need them all, call it, if not use a direct call to the
# section.

class ModulesDemo():
    def DemoModules(self):
        print(math.sqrt(400)) #Case 1. square root, I will call it this way if the import above is 'import math'
        print(sqrt(100)) #Case 2. I will call it this way if the import above is 'import math'

    def Car_description(self):
        make  = "BMW"
        model = "e750"
        Car.info(make, model) #using the 'Car' alias to show the info.
        #info(make, model)  # using the 2nd way to import, directly calling the method


m = ModulesDemo()
m.DemoModules()
m.Car_description()