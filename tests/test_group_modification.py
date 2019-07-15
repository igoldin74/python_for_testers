from model.group import Group


def test_group_modification(app):
    app.session.login()
    app.group.open_group_page()
    app.group.modify_first_group(Group(name='edited_group_name',
                                       header='edited_group_header',
                                       footer='edited_group_footer'))
    app.open_home_page()
    app.session.logout()
