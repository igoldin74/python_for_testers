from contact import Contact
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_new_contact_creation(app):
    app.login()
    app.create_new_contact(Contact(firstname="test_contact1",
                                              middlename="test_middle_name1",
                                              lastname="test_last_name1",
                                              homephone="234567777",
                                              mobilephone="678765555",
                                              email="test1@mailinator.com"))
    app.open_home_page()
    app.logout()
