
"""
to run python -m pytest -v -s Example/test_reporting_demo.py --browser firefox

to generate html report use this command:
python -m pytest -v -s Example/test_reporting_demo.py --browser firefox --html=HTML_REPORT.html
python -m pytest -v -s Example/test_reporting_demo.py --browser firefox --html=HTML_REPORT.html --capture sys -rP -rF



"""


import pytest
from Example.Class_to_test import SomeClassToTest

@pytest.mark.usefixtures("oneTimeSetUp","setUp") #put the fixture at class level in case we have many methods
class TestReportingDemo():

    @pytest.fixture(autouse = True) #anyplace will use this fixture.
    def classSetup(self):
        self.abc = SomeClassToTest(10)


    def test_method_A(self):
        result = self.abc.sumNumbers(2,8) #calling the method from the other class to execute the sum
        assert result == 20 #assert that the result is 20, using pytest, will show output on the console if it fails
        print("Running method A")

    def test_method_B(self):
        result = self.abc.sumNumbers(2,8) #calling the method from the other class to execute the sum
        assert result > 20 #assert that the result is 20, using pytest, will show output on the console if it fails


        print("Running method B")
