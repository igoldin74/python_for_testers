from model.contact import Contact


def test_first_contact_deletion(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="new_contact_first_name"))

    app.contact.delete()


