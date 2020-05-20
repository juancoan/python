import pytest

@pytest.yield_fixture() #decorator to run BEFORE & AFTER every method
def setUp():
    print("Print Demo statement BEFORE - setUp")
    yield #has to be included to indicate what will run after every method.
    print("Print Demo statement AFTER - teardown")



# Writting the method like this on the 'conftest' file, will allow the setup and teardown to be executed only
# once.
# Name the method 'oneTimeSetup', then on the test files, add the parameter to have it run there.
#Also add 'scrop = 'module' to the method
#by default the scope = function, to apply to all methods, but changing it to module, it will apply it one before
# and after running the whole file-test

@pytest.yield_fixture(scope="module") #decorator to run BEFORE & AFTER every method
def oneTimeSetUp():
    print("Print confTest statement BEFORE - ONE TIME setUp")
    yield #has to be included to indicate what will run after every method.
    print("Print confTest statement AFTER - ONE TIME teardown")
