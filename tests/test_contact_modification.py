from model.contact import Contact
from random import randrange
import re


def test_random_contact_modification(app):
    contact = Contact(firstname="test_contact1_modified",
                              middlename="test_middle_name1_modified",
                              lastname="test_last_name1_modified",
                              homephone="234567777_new",
                              email1="test@tester.com")
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
                              email1="tester@test.org")
    if app.contact.count() == 0:
        app.contact.create(contact)
    old_contact_list = app.contact.get_contact_list()
    contact.id = old_contact_list[0].id
    app.contact.modify_first_contact(contact)
    assert app.contact.count() == len(old_contact_list)
    new_contact_list = app.contact.get_contact_list()
    old_contact_list[0] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


def test_contact_details_match_on_home_and_edit_pages(app):
    details_from_home_page = app.contact.get_contact_list()[0]
    details_from_edit_page = app.contact.get_contact_details_from_edit_page(0)
    print(details_from_edit_page)
    print(details_from_home_page)
    assert details_from_home_page.firstname == details_from_edit_page.firstname
    assert details_from_home_page.lastname == details_from_edit_page.lastname
    assert details_from_home_page.address == details_from_edit_page.address
    assert details_from_home_page.all_emails == concatenate_emails(details_from_edit_page)
    assert details_from_home_page.all_phones == concatenate_phones(details_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def concatenate_emails(contact):
    return "\n".join([contact.email1, contact.email2, contact.email3])


def concatenate_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                [contact.homephone, contact.mobilephone, contact.workphone, contact.phone2]))))




