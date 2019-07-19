

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        self.fill_out_group_form(group)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.select_first_group()
        wd.find_element_by_name("delete").click()

    def modify_first_group(self, group):
        wd = self.app.wd
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_out_group_form(group)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("groups").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='selected[]']").click()

    def fill_out_group_form(self, group):
        self.app.type("group_name", group.name)
        self.app.type("group_header", group.header)
        self.app.type("group_footer", group.footer)


