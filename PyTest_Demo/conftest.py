import pytest

@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class") #can be session, module, class
def oneTimeSetUp(request, browser, osType):
    print("Running one time setUp")
    if browser == 'firefox':
        value = 10 #SomeClassToTest() class parameter to validate with assert, based on condittion
        print("Running tests on FF")
    else:
        value = 20 #SomeClassToTest() class parameter to validate with assert
        print("Running tests on chrome")

    if request.cls is not None: #class atribute from the request is not NONE
        request.cls.value = value #will make it class atribute
    yield value
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")


"""
import pytest

@pytest.fixture() #decorator to run BEFORE & AFTER every method
def setUp():
    print("Print method level statement BEFORE - setUp")
    yield #has to be included to indicate what will run after every method.
    print("Print method level statement AFTER - teardown")



# Writting the method like this on the 'conftest' file, will allow the setup and teardown to be executed only
# once.
# Name the method 'oneTimeSetup', then on the test files, add the parameter to have it run there.
#Also add 'scope = 'module' to the method
#by default the scope = function, to apply to all methods, but changing it to module, it will apply it one before
# and after running the whole file-test

@pytest.fixture(scope="module") #decorator to run BEFORE & AFTER every method
def oneTimeSetUp(browser,osType): #obtain the fixtures at this moment
    print("Print confTest statement BEFORE - ONE TIME setUp")
    if browser == 'firefox':
        print("Running the tests on FF")
    else:
        print("Running tests on other browser")
    yield #has to be included to indicate what will run after every method.
    print("Print confTest statement AFTER - ONE TIME teardown")


Creating 2 cmd line arguments 

def pytest_add_option(parser):
    parser.addoption("--browser") #adds an option to the parser variable, from the command line, like browser
    parser.addoption("--osType", help = "Indicate OS type")  # adds an option to the parser variable, from the command line, like OS

#method to take the option and create it as a fixture
@pytest.fixture(scope="session")
def browser(request): #request it, special keyword
    return request.config.getoption("--browser") #return the whatever we inserted on the cmdline for --browser

#method to take the option and create it as a fixture
@pytest.fixture(scope="session")
def osType(request): #request it
    return request.config.getoption("--osType") #return the whatever we inserted on the cmdline for --browser

"""