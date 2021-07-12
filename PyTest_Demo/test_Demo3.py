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
import pytest

@pytest.fixture() #decorator to run BEFORE & AFTER every method
def setUp():
    print("Runs Setup D3 ONCE BEFORE EVERY method - setUp")
    yield #has to be included to indicate what will run after every method.
    print("Runs Setup D3 ONCE AFTER EVERY method - teardown")

def test_demo3_MethodA(setUp): #addung the name of the method that is a fixture
    print("Method A - Demo 3")

def test_demo3_MethodB(setUp): #addung the name of the method that is a fixture
    print("Method B - Demo 3")