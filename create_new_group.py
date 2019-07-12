import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_group_creation(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="test_group_0", header="dfdsfsdfg", footer="sdgdsfdsf"))
    app.logout()


