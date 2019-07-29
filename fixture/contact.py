import random


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_out_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def delete(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")

    def modify(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_out_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()

    def modify_random(self, contact):
        xpath_locator = self.get_random_contact_id()
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath(xpath_locator).click()
        self.fill_out_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()

    def get_random_contact_id(self):
        wd = self.app.wd
        elements = wd.find_elements_by_xpath("//a[contains(@href, 'edit.php?id')]")
        links = []
        for i in elements:
            link = i.get_attribute('href')
            links.append(link)
        url = random.choice(links)
        contact_id = url[49:51]
        xpath_locator = "//a[@href='edit.php?id=" + contact_id + "']"
        print(xpath_locator)
        return xpath_locator

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
