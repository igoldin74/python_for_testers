from selenium import webdriver
import unittest


class NewGroupCreation(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_group_creation(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_group_page(wd)
        self.init_group_creation(wd)
        self.fill_group_form(wd)
        self.submit_group_form(wd)
        self.open_group_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def submit_group_form(self, wd):
        wd.find_element_by_name("submit").click()

    def fill_group_form(self, wd):
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("test_group_0")
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("dfdsfsdfg")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("sdgdsfdsf")

    def init_group_creation(self, wd):
        wd.find_element_by_name("new").click()

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://192.168.1.13:8080/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
