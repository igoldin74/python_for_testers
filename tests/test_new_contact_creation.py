from model.contact import Contact


def test_new_contact_creation(app):
    app.contact.create(Contact(firstname="test_contact1",
                              middlename="test_middle_name1",
                              lastname="test_last_name1",
                              homephone="234567777",
                              mobilephone="678765555",
                              email="test1@mailinator.com"))
    app.open_home_page()
