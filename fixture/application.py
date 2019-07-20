from selenium import webdriver
from fixture.session import SessionHelper
from fixture.contact import ContactHelper
from fixture.group import GroupHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        if wd.current_url.endswith("/index.php") and len(wd.find_elements_by_id("MassCB")) > 0:
            return
        wd.find_element_by_link_text("home").click()

    def destroy(self):
        self.wd.quit()

    def type(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def is_not_valid(self):
        try:
            self.wd.current_url
            return False
        except:
            return True


