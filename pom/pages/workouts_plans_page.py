from QA_Python_Diploma.pom.pages.base_page import BasePage
from QA_Python_Diploma.pom.pages.locators import workouts_pages_locators as w_loc


class WorkoutsPlansPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def menu_field(self):
        return self.find_element(w_loc.menu)

    def open(self):
        self.driver.get('https://wodcat.com/')

    @property
    def workouts_plans(self):
        return self.find_element(w_loc.workouts_plans)

    @property
    def workouts_plans_logo(self):
        return self.find_element(w_loc.workouts_plans_logo)

    @property
    def user_name_field(self):
        return self.find_element(w_loc.user_name_field)

    @property
    def month(self):
        return self.find_element(w_loc.month)

    @property
    def month_arrow_right(self):
        return self.find_element(w_loc.month_arrow_right)

    @property
    def window_workout(self):
        return self.find_element(w_loc.window_workout)

    @property
    def add_new_workout(self):
        return self.find_element(w_loc.add_new_workout)

    @property
    def simple_wod(self):
        return self.find_element(w_loc.simple_wod)

    @property
    def header(self):
        return self.find_element(w_loc.header)

    @property
    def wod_scoring(self):
        return self.find_element(w_loc.wod_scoring)

    @property
    def select_panel(self):
        return self.find_element(w_loc.select_panel)

    @property
    def strength(self):
        return self.find_element(w_loc.strength)

    @property
    def modality(self):
        return self.find_element(w_loc.modality)

    @property
    def select_panel_two(self):
        return self.find_element(w_loc.select_panel_two)

    @property
    def description(self):
        return self.find_element(w_loc.description)

    @property
    def number_of_rounds(self):
        return self.find_element(w_loc.number_of_rounds)

    @property
    def time_limit(self):
        return self.find_element(w_loc.time_limit)

    @property
    def save_button(self):
        return self.find_element(w_loc.save_button)

    @property
    def workout_calendar(self):
        return self.find_element(w_loc.workout_calendar)

    @property
    def workout_full(self):
        return self.find_element(w_loc.workout_full)

    @property
    def workout_action(self):
        return self.find_element(w_loc.workout_action)

    @property
    def delete_workout(self):
        return self.find_element(w_loc.delete_workout)

    @property
    def discussion(self):
        return self.find_element(w_loc.discussion)

    @property
    def type_a_comment(self):
        return self.find_element(w_loc.type_a_comment)

    @property
    def green_submit(self):
        return self.find_element(w_loc.green_button)

    @property
    def comment_list(self):
        return self.find_element(w_loc.comment_list)

    @property
    def real_comment(self):
        return self.find_element(w_loc.real_comment)

    @property
    def delete_comment(self):
        return self.find_element(w_loc.delete_comment)

    @property
    def settings(self):
        return self.find_element(w_loc.settings)

    @property
    def change_user_name(self):
        return self.find_element(w_loc.name_field)

    @property
    def button_save(self):
        return self.find_element(w_loc.button_save)

    @property
    def updated(self):
        return self.find_element(w_loc.updated)
