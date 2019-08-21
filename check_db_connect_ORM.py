from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="192.168.1.22", database="addressbook", user="admin", password="admin")

try:
    l = db.get_group_list()
    for item in l:
      print(item)
    print(len(l))
    lc = db.get_contact_list()
    for item in lc:
        print(item)
    print(len(lc))
finally:
   pass

try:
    lcg = db.get_contacts_in_group(Group(id="23"))
    for item in lcg:
        print(item)
    print(len(lcg))

    lcng = db.get_contacts_not_in_group(Group(id="23"))
    for item in lcng:
        print(item)
    print(len(lcng))
finally:
    pass

