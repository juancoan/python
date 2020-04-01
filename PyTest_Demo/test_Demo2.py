"""
ALWAYS import pytest
To run the test using pytest on cmd:
    python -m pytest -v -s  FileName.py (-v -s switches are to provide verbosity)
    python -m pytest FileName.py

On the setUp() method, you have to add a PyTest decorator, to make it like a fixture run before & after methods)
    @pytest.yield_fixture() this is the decorator that has to be on the method that is the one running before/after
    the name of the method, has to be put as a param on the method where it has to run before.
    also the word "yield" has to be added on that method and then whatever I want to run AFTER.
"""
import pytest

@pytest.yield_fixture() #decorator to run BEFORE & AFTER every method
def setUp():
    print("Runs D2 ONCE BEFORE EVERY method")
    yield #has to be included to indicate what will run after every method.
    print("Runs D2 ONCE AFTER EVERY method")

def test_demo2_MethodA(setUp): #addung the name of the method that is a fixture
    print("Method A - Demo 2")


def test_demo2_MethodB(setUp): #addung the name of the method that is a fixture
    print("Method B - Demo 2")