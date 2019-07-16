from model.contact import Contact


def test_first_contact_modification(app):
    app.session.login()
    app.contact.modify(Contact(firstname="test_contact1_modified",
                              middlename="test_middle_name1_modified",
                              lastname="test_last_name1_modified",
                              homephone="234567777_new",
                              mobilephone="678765555_new",
                              email="test1@mailinator.com_new"))
    app.open_home_page()
    app.session.logout()


def test_random_contact_modification(app):
    app.session.login()
    app.contact.modify_random(Contact(firstname="random",
                              middlename="random",
                              lastname="random",
                              homephone="random",
                              mobilephone="random",
                              email="test1@random.com_new"))
    app.session.logout()
