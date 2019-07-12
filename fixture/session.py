

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username="admin", password="secret"):
        wd = self.app.wd
        self.app.open_home_page()
        wd.get("http://192.168.1.22:8080/addressbook/index.php")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()