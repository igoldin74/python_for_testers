import pytest
from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        browser = request.config.getoption('--browser')
        baseurl = request.config.getoption('--baseurl')
        fixture = Application(browser=browser, baseurl=baseurl)
    elif fixture.is_not_valid():
        fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--baseurl', action='store', default='http://192.168.1.22:8080/addressbook/index.php')
