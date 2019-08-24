from model.group import Group
from random import randrange
import random


def test_group_modification(app):
    group = Group(name="test_group_0", header="dfdsfsdfg", footer="sdgdsfdsf")
    if app.group.count() == 0:
        app.group.create(group)
    app.group.open_group_page()
    old_group_list = app.group.get_group_list()
    index = randrange(len(old_group_list))
    group.id = old_group_list[index].id
    app.group.modify_group_by_index(group, index)
    assert len(old_group_list) == app.group.count()
    new_group_list = app.group.get_group_list()
    old_group_list[index] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


def test_group_modification_with_db_assertion(app, db, check_ui):
    old_group_list = db.get_group_list()
    group_data = Group(name="test_damn_group", header="damn_header", footer="damn_footer")
    if len(old_group_list) == 0:
        app.group.create(group_data)
        old_group_list = db.get_group_list()
    app.group.open_group_page()
    group = old_group_list[0]
    app.group.modify_group_by_id(group_data, group.id)
    assert len(old_group_list) == app.group.count()
    new_group_list = db.get_group_list()
    #  idx = old_group_list.index(group)
    del old_group_list[0]
    old_group_list.insert(0, group_data)
    assert old_group_list == new_group_list
    if check_ui:  # this will execute when "--check_ui" run option is added
        def clean(group):  # this func removes spaces from group names
            return Group(id=group.id, name=group.name.strip())

        db_list = map(clean, new_group_list)
        assert sorted(db_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
