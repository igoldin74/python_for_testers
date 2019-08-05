from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(maxlen):
    symbols = string.digits
    return "-".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Contact(firstname=random_string("name", 5),
                     middlename=random_string("middlename", 5),
                     lastname=random_string("lastname", 5),
                     homephone=random_string("homephone", 5),
                     mobilephone=random_string("mobile", 5),
                     email1=random_string("email", 5))
             for i in range(5)
             ]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_new_contact_creation(app, contact):
    old_contact_list = app.contact.get_contact_list()
    app.contact.create(contact)
    assert app.contact.count() == len(old_contact_list) + 1
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(old_contact_list, key=Contact.id_or_max)
