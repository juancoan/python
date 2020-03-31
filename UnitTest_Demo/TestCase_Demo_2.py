"""
This will have the Setup & the tearDown methods run ONCE and not on every/after test
Using the setupClass & tearDownClass classes will make it run only ONCE before & after the tests
Using the setUp & tearDown will execute each time before/after the tests are run.
"""
import unittest

class Test_Case_Demo_2(unittest.TestCase):#Inheriting from the Test Case class on unitTest to use it

    @classmethod #DECORATOR - it is like an annotation, used to override and be able to use it.
    def setUpClass(self):
        print("*-#"*30)
        print("I will run ONLY ONCE before every test")
        print("*-#" * 30)

    #Test methods should be named starting with "test" so testrunner knows it is and will run it.
    def test_MethodA(self):
        print("Running method_A")

    def test_MethodB(self):
        print("Running method_B")

    @classmethod  # DECORATOR - it is like an annotation
    def tearDownClass(self):
        print("*-#" * 30)
        print("I will run ONLY ONCE after every test")
        print("*-#" * 30)

    #Making the call to run the tests.
    if __name__ == '__main__':
        unittest.main(verbosity=2)
