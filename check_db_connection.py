import pymysql.cursors
from fixture.db import DbFixture

connection = pymysql.connect(host="192.168.1.22", database="addressbook", user="admin", password="admin")

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()


db = DbFixture(host="192.168.1.22", database="addressbook", user="admin", password="admin")

try:
    groups = db.get_group_list()
    for group in groups:
        print(group)
    print(len(groups))
#finally:
    #db.destroy()

#try:
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()
