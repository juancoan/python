"""
ALWAYS import pytest
To run the test using pytest on cmd:
    python -m pytest -v -s  FileName.py (-v -s switches are to provide verbosity)
    python -m pytest FileName.py

On the setUp() method, you have to add a PyTest decorator, to make it like a fixture run before & after methods)
    @pytest.fixture() this is the decorator that has to be on the method that will run before
    the name of the method, has to be put as a param on the method where it has to run before.
"""
import pytest

@pytest.fixture() #decorator
def setUp():
    print("Runs Setup D1 ONCE before EVERY method")

def test_MethodA(setUp): #addung the name of the method that is a fixture
    print("Method A - Demo 1")


def test_MethodB(setUp): #addung the name of the method that is a fixture
    print("Method B - Demo 1")