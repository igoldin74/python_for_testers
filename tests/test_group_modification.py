from model.group import Group


def test_group_modification(app):
    if app.group.count() == 0:
        app.group.create(Group(name="newly_created_group"))
    app.group.open_group_page()
    app.group.modify_first_group(Group(name='edited_group_name'))
    app.open_home_page()
