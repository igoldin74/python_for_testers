from model.contact import Contact


def test_new_contact_creation(app, json_contacts):
    contact = json_contacts
    old_contact_list = app.contact.get_contact_list()
    app.contact.create(contact)
    assert app.contact.count() == len(old_contact_list) + 1
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
