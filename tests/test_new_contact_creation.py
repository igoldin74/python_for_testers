from model.contact import Contact
import allure

@allure.title("Test a new contact entry can be created in addressbook")
def test_new_contact_creation(app, json_contacts):
    contact = json_contacts
    old_contact_list = app.contact.get_contact_list()
    @allure.step("Given a contact list")
    def step_1():
        return old_contact_list
    step_1()
    @allure.step("When I add a contact %s to the list" % contact)
    def step_2(contact):
        app.contact.create(contact)
    step_2(contact)
    @allure.step("The new contact list is equal to the old one with added contact")
    def step_3(old_contact_list, contact):
        assert app.contact.count() == len(old_contact_list) + 2
        new_contact_list = app.contact.get_contact_list()
        old_contact_list.append(contact)
        assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    step_3(old_contact_list, contact)

@allure.title("Test a new contact entry can be created in addressbook and assert in DB")
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