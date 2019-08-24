from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

db = ORMFixture(host="192.168.1.22", database="addressbook", user="admin", password="admin")


def test_remove_contact_from_group(app):
    contact_list = db.get_contact_list()
    group_list = db.get_group_list()
    if len(contact_list) == 0:
        app.contact.create(Contact(firstname="test_contact1_modified", lastname="test_last_name1_modified"))
        contact_list = db.get_contact_list()
    if len(group_list) == 0:
        app.group.create(Group(name="test_group_random_name", header="random_header", footer="random_footer"))
        group_list = db.get_group_list()
    group = random.choice(group_list)  # got random group
    contacts_in_group = db.get_contacts_in_group(group)  # got list of contacts that are in random group
    if len(contacts_in_group) == 0:
        contact_to_add = random.choice(contact_list)
        app.contact.add_contact_to_group(contact_to_add.id, group.id)
        contacts_in_group = db.get_contacts_in_group(group)
    contact = random.choice(contacts_in_group)  # got contact from the list of contacts
    app.contact.remove_contact_from_group(contact.id, group.id)
    contacts_not_in_group = db.get_contacts_not_in_group(group)  # got list of contacts not in this group
    assert contact in contacts_not_in_group

