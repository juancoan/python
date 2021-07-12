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

#setUp and tearDown fixture are located now on the conftest.py file on the same package
# install the pytest-order plugin to deal with the ordering

@pytest.mark.order(2) #Fixture to handle the order for this method to run
def test_demo2_ConfTestA(oneTimeSetUp, setUp): #addung the name of the method that is a fixture
    print("Running ConfTest A Demo 2- ConfTest")

@pytest.mark.order(3) #Fixture to handle the order for this method to run
def test_demo2_ConfTestB(oneTimeSetUp, setUp): #addung the name of the method that is a fixture
    print("Running ConfTest B Demo 2 - ConfTest")

@pytest.mark.order(1) #Fixture to handle the order for this method to run
def test_demo2_ConfTestC(oneTimeSetUp, setUp): #addung the name of the method that is a fixture
    print("Running ConfTest C Demo 2- ConfTest")

@pytest.mark.order(6) #Fixture to handle the order for this method to run
def test_demo2_ConfTestD(oneTimeSetUp, setUp): #addung the name of the method that is a fixture
    print("Running ConfTest D Demo 2 - ConfTest")

@pytest.mark.order(4) #Fixture to handle the order for this method to run
def test_demo2_ConfTestE(oneTimeSetUp, setUp): #addung the name of the method that is a fixture
    print("Running ConfTest E Demo 2- ConfTest")

@pytest.mark.order(5) #Fixture to handle the order for this method to run
def test_demo2_ConfTestF(oneTimeSetUp, setUp): #addung the name of the method that is a fixture
    print("Running ConfTest F Demo 2 - ConfTest")