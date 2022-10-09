from QA_Python_Diploma.pom.pages.base_page import BasePage
from QA_Python_Diploma.pom.pages.locators import profile_page_locators as loc


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def menu_field(self):
        return self.find_element(loc.menu)

    def open(self):
        self.driver.get('https://wodcat.com/')

    @property
    def logo(self):
        return self.find_element(loc.logo)

    @property
    def profile_and_settings(self):
        return self.find_element(loc.profile_and_settings)

    @property
    def see_profile(self):
        return self.find_element(loc.see_profile)

    @property
    def user_name(self):
        return self.find_element(loc.user_name)

    @property
    def user_name_input(self):
        return self.find_element(loc.first_name)

    @property
    def img(self):
        return self.find_element(loc.img)

    @property
    def gender(self):
        return self.find_element(loc.gender)

    @property
    def redact_profile(self):
        return self.find_element(loc.redact_profile)

    @property
    def heading(self):
        return self.find_element(loc.heading)

    @property
    def save_button(self):
        return self.find_element(loc.button_save)

    @property
    def saved(self):
        return self.find_element(loc.saved)

    @property
    def instagram(self):
        return self.find_element(loc.instagram)

    @property
    def table(self):
        return self.find_element(loc.table)

    @property
    def error(self):
        return self.find_element(loc.error)

    @property
    def facebook(self):
        return self.find_element(loc.facebook)

    @property
    def twitter(self):
        return self.find_element(loc.twitter)

    @property
    def social_network_on_the_main_page(self):
        return self.find_element(loc.social_network_on_the_main_page)
