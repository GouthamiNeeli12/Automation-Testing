# import pytest
#
#
# def test_greetCreditCard():
#     print("Hello")
#
# @pytest.mark.smoke
# def test_demo2(setup):
#     a=10
#     b=3
#     print(a+b)
#
# @pytest.mark.xfail
# def test_asserting():
#     msg="Hello"
#     assert msg=="Hi","strings do not match"

def test_crossbrowser(crossBrowser):
    print(crossBrowser)