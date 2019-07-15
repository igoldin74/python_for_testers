

def test_first_contact_deletion(app):
    app.session.login()
    app.contact.delete()
    app.open_home_page()
    app.session.logout()

