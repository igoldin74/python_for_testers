from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_out_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(contact, 0)

    def modify_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_out_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def fill_out_contact_form(self, contact):
        self.app.type("firstname", contact.firstname)
        self.app.type("middlename", contact.middlename)
        self.app.type("lastname", contact.lastname)
        self.app.type("home", contact.homephone)
        self.app.type("mobile", contact.mobilephone)
        self.app.type("email", contact.email)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                firstname = element.find_element_by_css_selector('[name] td:nth-of-type(3)').text
                lastname = element.find_element_by_css_selector('[name] td:nth-of-type(2)').text
                address = element.find_element_by_css_selector('[name] td:nth-of-type(4)').text
                emails = element.find_element_by_css_selector('[name] td:nth-of-type(5)').text
                phones = element.find_element_by_css_selector('[name] td:nth-of-type(6)').text
                contact_id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, 
                                                  id=contact_id, address=address, all_phones=phones, all_emails=emails))
            return list(self.contact_cache)

    def get_contact_details_from_edit_page(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        contact_id = wd.find_element_by_name("id").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=contact_id, address=address, email1=email1,
                       email2=email2, email3=email3, homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                       phone2=phone2)

