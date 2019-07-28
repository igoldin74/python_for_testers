from model.group import Group


def test_group_modification(app):
    group = Group(name="test_group_0", header="dfdsfsdfg", footer="sdgdsfdsf")
    if app.group.count() == 0:
        app.group.create(group)
    app.group.open_group_page()
    old_group_list = app.get_group_list()
    group.id = old_group_list[0].id
    app.group.modify_first_group(group)
    new_group_list = app.get_group_list()
    app.open_home_page()
    assert len(old_group_list) == len(new_group_list)
    old_group_list[0] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)

