from model.contact import Contact


def test_new_contact_creation(app):
    contact = Contact(firstname="test_contact1",
                              middlename="test_middle_name1",
                              lastname="test_last_name1",
                              homephone="234567777",
                              mobilephone="678765555",
                              email="test1@mailinator.com")
    old_contact_list = app.get_contact_list()
    app.contact.create(contact)
    new_contact_list = app.get_contact_list()
    app.open_home_page()
    assert len(new_contact_list) == len(old_contact_list) + 1
    old_contact_list.append(contact)
    assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(old_contact_list, key=Contact.id_or_max)
