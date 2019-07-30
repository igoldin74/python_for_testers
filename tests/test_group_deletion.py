from model.group import Group


def test_group_removal(app):
    old_group_list = app.group.get_group_list()
    group = Group(name="test_group_0", header="dfdsfsdfg", footer="sdgdsfdsf")
    if app.group.count() == 0:
        app.group.create(group)
    app.group.open_group_page()
    app.group.delete_first_group()
    assert app.group.count() == len(old_group_list) - 1
    new_group_list = app.group.get_group_list()
    old_group_list[0:1] = []
    assert old_group_list == new_group_list
