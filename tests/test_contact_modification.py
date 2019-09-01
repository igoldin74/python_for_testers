from model.contact import Contact
from random import randrange
import random
import re
from fixture.orm import ORMFixture

orm_db = ORMFixture(host="localhost", database="addressbook", user="root", password="") # connection to DB via PonyORM initialized here


def test_random_contact_modification(app):
    old_contact_list = app.contact.get_contact_list()
    contact = Contact(firstname="test_contact1_modified",
                              middlename="test_middle_name1_modified",
                              lastname="test_last_name1_modified",
                              homephone="234567777_new",
                              email1="test@tester.com")
    if app.contact.count() == 0:
        app.contact.create(contact)
    index = randrange(len(old_contact_list))
    contact.id = old_contact_list[index].id
    app.contact.modify_contact_by_index(contact, index)
    assert app.contact.count() == len(old_contact_list)
    new_contact_list = app.contact.get_contact_list()
    old_contact_list[index] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


def test_contact_modification_loaded_from_db(app, db, check_ui):
    old_contact_list = db.get_contact_list()
    contact_data = Contact(firstname="test_contact1_modified",
                              middlename="test_middle_name1_modified",
                              lastname="test_last_name1_modified",
                              homephone="234567777_new",
                              email1="test@tester.com")
    contact = random.choice(old_contact_list)
    if len(old_contact_list) == 0:
        app.contact.create(contact)
        old_contact_list = db.get_contact_list()
    app.contact.modify_contact_by_id(contact_data, contact.id)
    assert app.contact.count() == len(old_contact_list)
    new_contact_list = db.get_contact_list()
    idx = old_contact_list.index(contact)
    del old_contact_list[idx]
    old_contact_list.insert(idx, contact_data)
    assert old_contact_list == new_contact_list
    if check_ui:
        def clean(contact):  # this func removes spaces from group names
            return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
        db_list = map(clean, new_contact_list)
        assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


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


def test_contacts_on_home_page_match_db(app):
    details_from_db = orm_db.get_contact_list_orm()
    details_from_home_page = app.contact.get_contact_list()
    db_list = map(clean, details_from_db)
    contact_from_hp = sorted(details_from_home_page, key=Contact.id_or_max)[0]
    contact_from_db = sorted(db_list, key=Contact.id_or_max)[0]
    assert contact_from_hp == contact_from_db
    for contact_hp, contact_db in zip(details_from_home_page, db_list):
        assert contact_hp.firstname == contact_db.firstname
        assert contact_hp.lastname == contact_db.lastname
        assert contact_hp.all_emails == concatenate_emails(contact_db)
        assert contact_hp.all_phones == concatenate_phones(contact_db)


def clean(contact):
    return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(),
                   homephone=contact.homephone, mobilephone=contact.mobilephone,
                   email1=contact.email1, email2=contact.email2, email3=contact.email3)


def clear(s):
    return re.sub("[() -]", "", s)


def concatenate_emails(contact):
    return "\n".join(filter(lambda x: x != "" and x is not None, [contact.email1, contact.email2, contact.email3]))


def concatenate_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                [contact.homephone, contact.mobilephone, contact.workphone, contact.phone2]))))




