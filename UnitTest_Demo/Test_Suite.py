#Import the unit test module
import unittest

#Import the classes from the package/file, where there are tests
from Code.UnitTest_Demo.TestCase_3 import Test_Case_Class_3
from Code.UnitTest_Demo.TestCase_Demo import Test_Case_Class

#Get all the tests from Test_Case_Class_3 & Test_Case_Class classes. Create objs TstClass1 & 2
TstClass1 = unittest.TestLoader().loadTestsFromTestCase(Test_Case_Class_3)
TstClass2 = unittest.TestLoader().loadTestsFromTestCase(Test_Case_Class)

#Create a test suite combining Test_Case_Class_3 & Test_Case_Class classes.
#Provide the tests as a list to the test suide method.
smoke_Test = unittest.TestSuite([TstClass1,TstClass2])


#Trigger the run/execution of the suite
unittest.TextTestRunner(verbosity=2).run(smoke_Test)#specify the test suite object