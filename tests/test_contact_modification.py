from model.contact import Contact
from random import randrange


def test_random_contact_modification(app):
    contact = Contact(firstname="test_contact1_modified",
                              middlename="test_middle_name1_modified",
                              lastname="test_last_name1_modified",
                              homephone="234567777_new",
                              mobilephone="678765555_new")
    if app.contact.count() == 0:
        app.contact.create(contact)
    old_contact_list = app.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    contact.id = old_contact_list[index].id
    app.contact.modify_contact_by_index(contact, index)
    assert app.contact.count() == len(old_contact_list)
    new_contact_list = app.contact.get_contact_list()
    old_contact_list[index] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


def test_first_contact_modification(app):
    contact = Contact(firstname="test_contact1_modified",
                              middlename="test_middle_name1_modified",
                              lastname="test_last_name1_modified",
                              homephone="234567777_new",
                              mobilephone="678765555_new")
    if app.contact.count() == 0:
        app.contact.create(contact)
    old_contact_list = app.contact.get_contact_list()
    contact.id = old_contact_list[0].id
    app.contact.modify_first_contact(contact)
    assert app.contact.count() == len(old_contact_list)
    new_contact_list = app.contact.get_contact_list()
    old_contact_list[0] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)

