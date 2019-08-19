import random
from model.group import Group


def test_group_removal(app, db, check_ui):
    old_group_list = db.get_group_list()
    group = random.choice(old_group_list)
    if len(db.get_group_list()) == 0:
        app.group.create(group)
    app.group.delete_group_by_id(group.id)
    assert app.group.count() == len(old_group_list) - 1
    new_group_list = db.get_group_list()
    old_group_list.remove(group)
    assert old_group_list == new_group_list
    if check_ui:  # this will execute when "--check_ui" run option is added
        def clean(group):  # this func removes spaces from group names
            return Group(id=group.id, name=group.name.strip())
        db_list = map(clean, new_group_list)
        assert sorted(db_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
