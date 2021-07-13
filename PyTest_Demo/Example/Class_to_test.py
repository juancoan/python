

#  the self variable represents the instance of the object itself.
class SomeClassToTest():

    def __init__(self,value): #class will take an argument, initialize the attributes of a class
        self.value = value

    def sumNumbers(self,a,b):
       return a + b + self.value