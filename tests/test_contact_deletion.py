from model.contact import Contact
from random import randrange


def test_random_contact_deletion(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="new_contact_first_name"))
    old_contact_list = app.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    app.contact.delete_contact_by_index(index)
    assert app.contact.count() == len(old_contact_list) - 1
    new_contact_list = app.contact.get_contact_list()
    old_contact_list[index:index+1] = []
    assert old_contact_list == new_contact_list


