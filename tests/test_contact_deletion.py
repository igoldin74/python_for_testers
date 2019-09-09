from model.contact import Contact
import random
import allure


@allure.title("Test a new contact entry can be deleted from addressbook")
def test_contact_removal(app, db, check_ui):
    old_contact_list = db.get_contact_list()
    contact = random.choice(old_contact_list)
    @allure.step("Apply prerequisites - create new contact entry")
    def create_contact(contact):
        app.contact.create(contact)
    if len(db.get_contact_list()) == 0:
        create_contact(Contact(firstname="new_contact_first_name"))
    @allure.step("Given a contact list")
    def step_1():
        return old_contact_list, contact
    step_1()
    @allure.step("When I delete a contact from addressbook")
    def step_2(contact):
        app.contact.delete_contact_by_id(contact.id)
        assert app.contact.count() == len(old_contact_list) - 1
    step_2(contact)
    @allure.step("Old contact list equals new contact list without deleted contact")
    def step_3(check_ui, contact):
        new_contact_list = db.get_contact_list()
        old_contact_list.remove(contact)
        assert old_contact_list == new_contact_list
        if check_ui:
            def clean(contact):  # this func removes spaces from group names
                return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
            db_list = map(clean, new_contact_list)
            assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    step_3(check_ui, contact)


