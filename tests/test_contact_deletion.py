from model.contact import Contact
import random


def test_contact_removal(app, db, check_ui):
    old_contact_list = db.get_contact_list()
    contact = random.choice(old_contact_list)
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="new_contact_first_name"))
    app.contact.delete_contact_by_id(contact.id)
    assert app.contact.count() == len(old_contact_list) - 1
    new_contact_list = db.get_contact_list()
    old_contact_list.remove(contact)
    assert old_contact_list == new_contact_list
    if check_ui:
        def clean(contact):  # this func removes spaces from group names
            return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
        db_list = map(clean, new_contact_list)
        assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


