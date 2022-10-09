from QA_Python_Diploma.pom.pages.base_page import BasePage
from QA_Python_Diploma.pom.pages.locators import home_page_locators as loc


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def member_login_button(self):
        return self.find_element(loc.member_login_button)

    def open(self):
        self.driver.get('https://wodcat.com')

    @property
    def enter_button(self):
        return self.find_element(loc.enter_button)

    @property
    def email_field(self):
        return self.find_element(loc.email_field)

    @property
    def password_field(self):
        return self.find_element(loc.password_field)

    @property
    def user(self):
        return self.find_element(loc.user)
