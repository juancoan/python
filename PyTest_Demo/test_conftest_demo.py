"""
ALWAYS import pytest
To run the test using pytest on cmd:
    python -m pytest -v -s  FileName.py (-v -s switches are to provide verbosity)
    python -m pytest FileName.py

On the setUp() method, you have to add a PyTest decorator, to make it like a fixture run before & after methods)
    @pytest.yield_fixture() this is the decorator that has to be on the method that is the one running before/after
    the name of the method, has to be put as a param on the method where it has to run before.
    also the word "yield" has to be added on that method and then whatever I want to run AFTER.

IMPORTANT:
---> File name, test name SHOULD both start with the word "test"

To run in different ways:
---> py.test test_mod.py ---> Runs test module
---> py.test somepath ---> Runs all tests below somepath
---> py.test test_module.py::test_method ---> Only runs test_method in test_module

adding the switches to the command:
-v ---> add verbosity
-s ---> to print statements
"""

"""
#setUp and tearDown fixture are located now on the conftest.py file on the same package
#On that same file there is a new method that is to run the setup/teardown only ONCE!, and
#the name of that method has to be added as a parameter on each test method, if you want ot use both or just 1,
#either to run before/after every test OR only ONCE before ALL test methods and only ONCE after all methods.

Using the conftest file where the setUP() method is, will have those methods there and will not need to be 
added here, so code is cleaner. When you run test_conftest_demo.py it will load that setUP() method from here

"""

import pytest

def test_demo1_ConfTestA(oneTimeSetUp, setUp): #addung the name of the method that is a fixture
    print("Running ConfTest A Demo 1 - ConfTest")

def test_demo1_ConfTestB(oneTimeSetUp, setUp): #addung the name of the method that is a fixture
    print("Running ConfTest B Demo 1 - ConfTest")