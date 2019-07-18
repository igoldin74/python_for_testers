

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
        wd.find_element_by_xpath("//input[@name='selected[]']").click()
        wd.find_element_by_name("delete").click()

    def modify_first_group(self, group):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='selected[]']").click()
        wd.find_element_by_name("edit").click()
        self.fill_out_group_form(group)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("groups").click()

    def fill_out_group_form(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
