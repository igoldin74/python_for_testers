from model.group import Group


def test_group_creation(app, db, json_groups, check_ui):
    group = json_groups
    old_group_list = db.get_group_list()
    app.group.create(group)
    assert app.group.count() == len(old_group_list) + 1
    new_group_list = db.get_group_list()
    old_group_list.append(group)
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    if check_ui:  # this will execute when "--check_ui" run option is added
        def clean(group):  # this func removes spaces from group names
            return Group(id=group.id, name=group.name.strip())

        db_list = map(clean, new_group_list)
        assert sorted(db_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



