from model.contact import Contact


def test_new_contact_creation(app, json_contacts):
    contact = json_contacts
    old_contact_list = app.contact.get_contact_list()
    app.contact.create(contact)
    assert app.contact.count() == len(old_contact_list) + 1
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


def test_new_contact_creation_assertion_from_db(app, json_contacts, db, check_ui):
    contact = json_contacts
    old_contact_list = db.get_contact_list()
    app.contact.create(contact)
    assert app.contact.count() == len(old_contact_list) + 1
    new_contact_list = db.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        def clean(contact):  # this func removes spaces from group names
            return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
        db_list = map(clean, new_contact_list)
        assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)