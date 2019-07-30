from model.group import Group
from random import randrange


def test_group_removal(app):
    old_group_list = app.group.get_group_list()
    group = Group(name="test_group_0", header="dfdsfsdfg", footer="sdgdsfdsf")
    if app.group.count() == 0:
        app.group.create(group)
    index = randrange(len(old_group_list))
    app.group.delete_group_by_index(index)
    assert app.group.count() == len(old_group_list) - 1
    new_group_list = app.group.get_group_list()
    old_group_list[index:index+1] = []
    assert old_group_list == new_group_list
