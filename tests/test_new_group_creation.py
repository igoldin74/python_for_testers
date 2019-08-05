from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Group(name=random_string("name", 5), header=random_string("header", 5), footer=random_string("footer", 5))
             for i in range(5)
             ]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_group_creation(app, group):
    old_group_list = app.group.get_group_list()
    app.group.create(group)
    assert app.group.count() == len(old_group_list) + 1
    new_group_list = app.group.get_group_list()
    old_group_list.append(group)
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)



