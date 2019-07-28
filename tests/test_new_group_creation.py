from model.group import Group


def test_group_creation(app):
    old_group_list = app.get_group_list()
    group = Group(name="test_group_0", header="dfdsfsdfg", footer="sdgdsfdsf")
    app.group.create(group)
    new_group_list = app.get_group_list()
    app.open_home_page()
    assert len(new_group_list) == len(old_group_list) + 1
    old_group_list.append(group)

    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)



