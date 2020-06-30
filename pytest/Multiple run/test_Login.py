import pytest

@pytest.yield_fixture()
def setup():
    print("going to the url")
    yield
    print("loging out")
def test_FBLogin(setup):
    print("login using Facebook")

def test_TwitterLogin(setup):
    print("login using Twitter")