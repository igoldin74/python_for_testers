

def test_first_contact_deletion(app):
    app.contact.delete()
    app.open_home_page()

