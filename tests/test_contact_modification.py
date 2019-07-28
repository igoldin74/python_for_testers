from model.contact import Contact


def test_first_contact_modification(app):
    contact = Contact(firstname="test_contact1_modified",
                              middlename="test_middle_name1_modified",
                              lastname="test_last_name1_modified",
                              homephone="234567777_new",
                              mobilephone="678765555_new")
    if app.contact.count() == 0:
        app.contact.create(contact)
    old_contact_list = app.get_contact_list()
    contact.id = old_contact_list[0].id
    app.contact.modify(contact)
    new_contact_list = app.get_contact_list()
    assert len(new_contact_list) == len(old_contact_list)
    app.open_home_page()
    old_contact_list[0] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


def test_random_contact_modification(app):
    contact = Contact(firstname="random",
                              middlename="random",
                              lastname="random",
                              homephone="random",
                              mobilephone="random",
                              email="test1@random.com_new")
    if app.contact.count() == 0:
        app.contact.create(contact)

    old_contact_list = app.get_contact_list()
    contact.id = old_contact_list[0].id
    app.contact.modify_random(contact)
    new_contact_list = app.get_contact_list()
    assert len(new_contact_list) == len(old_contact_list)
    old_contact_list[0] = contact
    assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(old_contact_list, key=Contact.id_or_max)


