from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
