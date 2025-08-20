import pytest

@pytest.mark.skip
@pytest.mark.usefixtures("dataLoad")
class Test_Example:
    def test_firstDemo(self,dataLoad):
        print(dataLoad)
        print("I am executing from first demo")

    def test_firstDemo1(self):
        print("I am executing from first demo1")

    def test_firstDemo2(self):
        print("I am executing from first demo2")

    def test_firstDemo3(self):
        print("I am executing from first demo3")
