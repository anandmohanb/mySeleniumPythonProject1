import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute BEFORE function")
    yield
    print("I will be executed AFTER testcase")

# @pytest.fixture()
# def dataloader():
#     return ["aaaa","bbbb","cccc"]

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul","Shetty","rahulshettyacademy.com"]

@pytest.fixture(params=["Chrome","Firefox","IE"])
def parameters(request):
    return request.param

@pytest.fixture(params=[("Chrome","anand","abc@123"),("Firefox","raju","pqr@123"),("IE","punnu","xyz@123")])
def multipleParams(request):
    return request.param