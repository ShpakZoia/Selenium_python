import pytest

@pytest.yield_fixture()
def setup():
    print("this will run once before every method")
    yield
    print("this will run once after every method")

def test_method1(setup):
    print("this is test method one")

def test_method2(setup):
    print("this is test method two")