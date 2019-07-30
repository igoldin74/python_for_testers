from model.group import Group


def test_group_creation(app):
    old_group_list = app.group.get_group_list()
    group = Group(name="test_group_0", header="dfdsfsdfg", footer="sdgdsfdsf")
    app.group.create(group)
    assert app.group.count() == len(old_group_list) + 1
    new_group_list = app.group.get_group_list()
    old_group_list.append(group)
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)



