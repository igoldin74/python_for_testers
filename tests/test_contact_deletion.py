from model.contact import Contact


def test_first_contact_deletion(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="new_contact_first_name"))
    old_contact_list = app.get_contact_list()
    app.contact.delete()
    assert app.contact.count() == len(old_contact_list) - 1
    new_contact_list = app.get_contact_list()
    old_contact_list[0:1] = []
    assert old_contact_list == new_contact_list


