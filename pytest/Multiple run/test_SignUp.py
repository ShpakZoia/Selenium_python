import pytest

@pytest.yield_fixture()
def setup():
    print("open browser to sign up")
    yield
    print("closing browser after sign up")

def test_Signup_FB(setup):
    print("sign up using Fb")

def test_Signup_Twitter(setup):
    print("sign up using Twitter")