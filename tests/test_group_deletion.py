from model.group import Group


def test_group_removal(app):
    if app.group.count() == 0:
        app.group.create(Group(name="newly_created_group"))
    app.group.open_group_page()
    app.group.delete_first_group()
