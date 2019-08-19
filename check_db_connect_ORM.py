from fixture.orm import ORMFixture

db = ORMFixture(host="192.168.1.22", database="addressbook", user="admin", password="admin")

try:
    l = db.get_group_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass

try:
    lc = db.get_contact_list()
    for item in lc:
        print(item)
    print(len(lc))
finally:
    pass

