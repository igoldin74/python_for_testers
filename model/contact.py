from sys import maxsize


class Contact:

    def __init__(self, firstname=None,
                 lastname=None,
                 middlename=None,
                 homephone=None,
                 mobilephone=None,
                 email=None,
                 id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.email = email
        self.id = id

    def __repr__(self):     # redefined standard representation method for printing out contact object in console
        return "%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.email)

    def __eq__(self, other):    # redefined standard equals method for comparing contact objects by their attributes
                                # (name&id)
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and \
               self.firstname == other.firstname and self.email == other.email

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
