import pytest


def test_method1():
    print("This is in method 1")

def test_method2(parameters):
    print("This is in method 2")
    print(parameters)

def test_method3(multipleParams):
    print("This is in method to display the multiple values in each run")
    print(multipleParams)