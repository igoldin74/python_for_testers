import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_group_creation(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="test_group_0", header="dfdsfsdfg", footer="sdgdsfdsf"))
    app.open_home_page()
    app.session.logout()


