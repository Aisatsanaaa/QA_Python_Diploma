from QA_Python_Diploma.pom.pages.base_page import BasePage
from QA_Python_Diploma.pom.pages.locators import workout_program_locators as p_loc


class WorkoutsProgramPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def menu_field(self):
        return self.find_element(p_loc.menu)

    def open(self):
        self.driver.get('https://wodcat.com/')

    def add_content(self):
        return self.find_element(p_loc.add_content)

    def create_w_program(self):
        return self.find_element(p_loc.create_w_program)

    def goal_window(self):
        return self.find_element(p_loc.goal_window)

    def publish_plan(self):
        return self.find_element(p_loc.publish_plan)

    def appeared_text(self):
        return self.find_element(p_loc.appeared_text)

    def next_button(self):
        return self.find_element(p_loc.next_button)

    def by_page(self):
        return self.find_element(p_loc.by_page)

    def plan_definition(self):
        return self.find_element(p_loc.plan_definition)

    def plan_definition_window(self):
        return self.find_element(p_loc.plan_definition)

    def online_coaching(self):
        return self.find_element(p_loc.online_coaching)

    def sport_discipline(self):
        return self.find_element(p_loc.sport_discipline)

    def fitness(self):
        return self.find_element(p_loc.fitness)
