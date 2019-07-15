

def test_group_removal(app):
    app.session.login()
    app.group.open_group_page()
    app.group.delete_first_group()
    app.session.logout()
