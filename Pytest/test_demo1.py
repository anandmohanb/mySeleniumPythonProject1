import pytest
from Pytest.BaseClass import BaseClass
# @pytest.mark.usefixtures("dataloader")

@pytest.mark.usefixtures("setup")
class TestExample(BaseClass):
    def test_firstFun(self):
        print("Hellow...first function in py test")

    def test_2ndFun(self):
        print("Hellow...2nd function in py test")
        assert True == False

    def test_thridFun(self):
        print("Hellow...3rd function in py test")
        log = self.getLogger()
        log.info("this is my info log message")
