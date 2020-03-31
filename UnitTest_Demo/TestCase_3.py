import unittest


class Test_Case_Class_3(unittest.TestCase):#Inheriting from the Test Case class on unitTest to use it

    #This will run before the actual test. No args, no params, nothing returned
    #Can be requisites, test data, logs, instance of the web browser, going to the site, etc
    def setUp(self):
        print("Will run once BEFORE every test.")

    #Test methods should be named starting with "test" so testrunner knows it is and will run it.
    def test_MethodA(self):
        print("Running method_A")

    def test_MethodB(self):
        print("Running method_B")

    #Used to cleanup values,
    def tearDown(self):
        print("Running AFTER every test.")

    #Making the call to run the tests.
    if __name__ == '__main__':
        unittest.main(verbosity=2)
