
# to run python -m pytest -v -s Example/test_class_demo.py --browser firefox

import pytest
from Example.Class_to_test import SomeClassToTest

@pytest.mark.usefixtures("oneTimeSetUp","setUp") #put the fixture at class level in case we have many methods
class TestClassDemo():

    @pytest.fixture(autouse = True) #anyplace will use this fixture.
    def classSetup(self):
        self.abc = SomeClassToTest(10)


    def test_method_A(self):
        result = self.abc.sumNumbers(2,8) #calling the method from the other class to execute the sum
        assert result == 19 #assert that the result is 20, using pytest, will show output on the console if it fails
        print("Running method A")

    def test_method_B(self):
        print("Running method B")
