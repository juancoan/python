"""
When running the tests, I can right click on several areas:
-> right click on the class part, it will run all the tests
-> right click on the 1st method, it will just run that method
-> right click on the 'if' condittion at the bottom, it will run the file.

IMPORTANT If it FAILS, then the next steps/actions will not be performed.

ASSERTION PAGE:
https://docs.python.org/3/library/unittest.html#unittest.TestCase


"""
import unittest
class Assert_Demo(unittest.TestCase):#Inheriting from the Test Case class on unitTest to use it

    #Test methods should be named starting with "test" so testrunner knows it is and will run it.
    # Still need to add the 'setupClass' and 'tearDownClass' methods

    #Test #1
    #The message is added to be shown when the test case FAILS!!!!
    def test_Assert_True_False(self):
        a = True
        self.assertTrue(a, "A is not True")
        b = True
        self.assertFalse(b, "B is not false")

    # Test #2
    # The message is added to be shown when the test case FAILS!!!!
    def test_Assert_Equal(self):
        a = "JuanCo"
        b = "JuanCo"
        self.assertEqual(a,b, "'A' is not equal to 'B'")

        # Test #3
        # The message is added to be shown when the test case FAILS!!!!
        # ALWAYS check the name of the assertion to have an idea of what it does should not do.
    def test_Assert_NOT_Equal(self):
        a = "JuanCo"
        b = "JuanCo"
        self.assertNotEqual(a, b, "'A' is EQUAL to 'B'")
        #It will fail because the purpose is make sure they are NOT equal.


    #Making the call to run the tests.
    if __name__ == '__main__':
        unittest.main(verbosity=2)
