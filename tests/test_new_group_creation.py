from model.group import Group


def test_group_creation(app):
    app.group.create(Group(name="test_group_0", header="dfdsfsdfg", footer="sdgdsfdsf"))
    app.open_home_page()


